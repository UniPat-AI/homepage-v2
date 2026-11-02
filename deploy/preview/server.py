#!/usr/bin/python3
"""Root-owned deployment entrypoint. Branch code runs only in restricted containers."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import urllib.request

sys.path.insert(0, '/usr/local/lib/unipat-preview')
from bundle import unpack
from client import branch_key, decode_branch

BASE = Path('/opt/unipat-previews')
CONFIG = Path('/etc/unipat-preview.json')
GATEWAY = 'unipat-preview-gateway'
NETWORK = 'unipat-preview'


def run(*args, **kwargs):
    return subprocess.run(list(args), check=True, text=True, timeout=kwargs.pop('timeout', 90), **kwargs)


def atomic_json(path, data):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data, sort_keys=True, indent=2) + '\n')
    temp.replace(path)


def generation(run_id, attempt):
    if not re.fullmatch('[1-9][0-9]{0,19}', run_id) or not re.fullmatch('[1-9][0-9]{0,5}', attempt):
        raise ValueError('Invalid workflow generation')
    return [int(run_id), int(attempt)]


def container_name(key, version):
    # Docker's embedded DNS requires each hostname label to fit in 63 characters.
    return 'up-' + key.rsplit('-', 1)[-1] + '-' + version


def nginx_text(host, container):
    # Both strings are constructed from validated identifiers, never raw ref names.
    if not re.fullmatch('[a-z0-9.-]+', host) or not re.fullmatch('[a-z0-9-]+', container):
        raise ValueError('Invalid route identifier')
    return '''server {
    listen 8080;
    server_name %s;
    add_header X-Robots-Tag "noindex, nofollow, noarchive" always;
    add_header Cache-Control "no-store" always;
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://%s:8000;
    }
}
''' % (host, container)


def reload_gateway():
    run('docker', 'exec', GATEWAY, 'nginx', '-t')
    run('docker', 'exec', GATEWAY, 'nginx', '-s', 'reload')


def remove_container(name):
    if name:
        run('docker', 'rm', '-f', name, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def check_health(host, commit):
    request = urllib.request.Request('http://127.0.0.1/_health', headers={'Host': host})
    with urllib.request.urlopen(request, timeout=8) as response:
        if json.load(response).get('release') != commit:
            raise RuntimeError('Preview health commit mismatch')


def stage_archive(archive, target, commit, upload_uid):
    fd = os.open(archive, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != upload_uid or info.st_size > 300 * 1024 * 1024:
            raise ValueError('Invalid upload')
        with os.fdopen(fd, 'rb', closefd=False) as src, tempfile.NamedTemporaryFile(dir=BASE / 'scratch') as safe:
            copied = 0
            while chunk := src.read(1024 * 1024):
                copied += len(chunk)
                if copied > 300 * 1024 * 1024:
                    raise ValueError('Upload exceeded size limit while being read')
                safe.write(chunk)
            safe.flush()
            unpack(safe.name, target, commit)
    finally:
        os.close(fd)


def parse_request(raw):
    if len(raw) > 2048:
        raise ValueError('Request too large')
    request = json.loads(raw)
    if not isinstance(request, dict) or request.get('action') not in ('deploy', 'remove'):
        raise ValueError('Invalid operation')
    keys = {'action', 'branch', 'run_id', 'attempt'}
    if request['action'] == 'deploy':
        keys.add('commit')
    if set(request) != keys or any(not isinstance(v, str) for v in request.values()):
        raise ValueError('Invalid request fields')
    decode_branch(request['branch'])
    generation(request['run_id'], request['attempt'])
    if request.get('commit') and not re.fullmatch('[0-9a-f]{40}', request['commit']):
        raise ValueError('Invalid commit')
    return request


def main():
    if os.geteuid() != 0 or len(sys.argv) != 1:
        raise SystemExit('The installed entrypoint accepts only a bounded JSON request on stdin')
    request = parse_request(sys.stdin.buffer.read(2049))
    action, token = request['action'], request['branch']
    if action not in ('deploy', 'remove'):
        raise ValueError('Invalid operation')
    branch = decode_branch(token)
    if branch == 'main':
        raise ValueError('main is production, not a preview')
    key = branch_key(branch)
    config = json.loads(CONFIG.read_text())
    host = key + '.' + config['domain']
    gen = generation(request['run_id'], request['attempt'])
    commit = request.get('commit')
    if commit and not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('Invalid commit')
    os.umask(0o022)
    with (BASE / 'deploy.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state_file = BASE / 'state' / (key + '.json')
        state = json.loads(state_file.read_text()) if state_file.exists() else {}
        if gen < state.get('generation', [0, 0]):
            print('Superseded deployment skipped')
            return
        route = BASE / 'nginx' / (key + '.conf')
        previous_route = route.read_text() if route.exists() else None
        if action == 'remove':
            route.unlink(missing_ok=True)
            try:
                reload_gateway()
            except BaseException:
                if previous_route is not None:
                    route.write_text(previous_route)
                raise
            remove_container(state.get('container'))
            shutil.rmtree(BASE / 'releases' / key, ignore_errors=True)
            atomic_json(state_file, {'branch': branch, 'generation': gen, 'deleted': True})
            print('Removed preview', key)
            return

        active = [p for p in (BASE / 'state').glob('*.json') if not json.loads(p.read_text()).get('deleted')]
        if not state.get('container') and len(active) >= config.get('max_previews', 10):
            raise RuntimeError('Preview capacity reached; delete unused branches first')
        version = commit[:12] + '-' + '-'.join(map(str, gen))
        container = container_name(key, version)
        target = BASE / 'releases' / key / version
        archive = BASE / 'incoming' / (key + '-' + version + '.tar.gz')
        if state.get('container') == container:
            check_health(host, commit)
            archive.unlink(missing_ok=True)
            print('Already deployed http://' + host)
            return
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        launched = False
        try:
            stage_archive(archive, target, commit, config['upload_uid'])
            if hashlib.sha256((target / 'requirements.lock').read_bytes()).hexdigest() != config['requirements_sha256']:
                raise RuntimeError('Runtime dependencies changed; rebuild the administrator-owned preview image first')
            run('docker', 'run', '-d', '--name', container, '--restart', 'unless-stopped',
                '--network', NETWORK, '--read-only', '--cap-drop', 'ALL',
                '--security-opt', 'no-new-privileges', '--pids-limit', '128',
                '--memory', '512m', '--cpus', '1', '--user', '65532:65532',
                '--tmpfs', '/tmp:rw,noexec,nosuid,size=128m,mode=1777',
                '--mount', 'type=bind,src=' + str(target) + ',dst=/app,readonly',
                '--env', 'PREVIEW_BRANCH=' + key, '--env', 'CDN_URL=',
                '--log-opt', 'max-size=10m', '--log-opt', 'max-file=2',
                '--label', 'unipat.preview.branch=' + key, config['runtime_image'],
                stdout=subprocess.DEVNULL)
            launched = True
            # Check the app directly from the gateway network before replacing the route.
            for attempt in range(30):
                result = subprocess.run(['docker', 'exec', GATEWAY, 'wget', '-qO-', 'http://' + container + ':8000/_health'], capture_output=True, text=True, timeout=10)
                try:
                    if result.returncode == 0 and json.loads(result.stdout).get('release') == commit:
                        break
                except ValueError:
                    pass
                if attempt == 29:
                    print(result.stderr[-2000:], file=sys.stderr)
                    logs = subprocess.run(['docker', 'logs', '--tail', '20', container], capture_output=True, text=True, timeout=10)
                    print(logs.stderr[-4000:], file=sys.stderr)
                    raise RuntimeError('New preview failed startup health check')
                time.sleep(1)
            route.write_text(nginx_text(host, container))
            reload_gateway()
            for attempt in range(10):
                try:
                    check_health(host, commit)
                    break
                except Exception:
                    if attempt == 9:
                        raise
                    time.sleep(1)
            atomic_json(state_file, {'branch': branch, 'generation': gen, 'commit': commit, 'container': container, 'url': 'http://' + host})
        except BaseException:
            if previous_route is None:
                route.unlink(missing_ok=True)
            else:
                route.write_text(previous_route)
            reload_gateway()
            if launched:
                remove_container(container)
            shutil.rmtree(target, ignore_errors=True)
            raise
        finally:
            archive.unlink(missing_ok=True)
        if state.get('container') and state['container'] != container:
            remove_container(state['container'])
        for old in target.parent.iterdir():
            if old != target:
                shutil.rmtree(old)
        print('Deployed http://' + host, commit)


if __name__ == '__main__':
    main()
