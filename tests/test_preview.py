import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deploy/preview'))
sys.path.insert(0, str(ROOT / 'deploy'))
from client import branch_key, encode_branch, decode_branch
spec = importlib.util.spec_from_file_location('preview_server', ROOT / 'deploy/preview/server.py')
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class PreviewTests(unittest.TestCase):
    def test_health_requires_exact_commit_and_rejects_caller_selected_urls(self):
        request = dict(action='health', branch=encode_branch('feature/test'), commit='a'*40, run_id='100', attempt='1')
        self.assertEqual(server.parse_request(json.dumps(request)), request)
        for bad in [dict(request, url='http://10.0.0.1'), dict(request, commit='bad'), dict(request, commit=''), {k:v for k,v in request.items() if k != 'commit'}]:
            with self.assertRaises(ValueError):
                server.parse_request(json.dumps(bad))

    def test_health_checks_local_gateway_and_exact_release(self):
        with patch.object(server.urllib.request, 'urlopen', return_value=io.BytesIO(b'{"release":"abc"}')) as fetch:
            self.assertEqual(server.check_health('up-test.example.com', 'abc'), {'release':'abc'})
            request = fetch.call_args.args[0]
            self.assertEqual(request.full_url, 'http://127.0.0.1/_health')
            self.assertEqual(request.get_header('Host'), 'up-test.example.com')
        with patch.object(server.urllib.request, 'urlopen', return_value=io.BytesIO(b'{"release":"old"}')):
            with self.assertRaises(RuntimeError):
                server.check_health('up-test.example.com', 'new')

    def test_cancelled_run_containers_are_pruned_without_removing_live_previews(self):
        with patch.object(server, 'run', return_value=SimpleNamespace(stdout='up-live\nup-abandoned\n')), patch.object(server, 'remove_container') as remove:
            server.prune_orphan_containers([{'container':'up-live'}, {'deleted':True}])
        remove.assert_called_once_with('up-abandoned')

    def test_container_hostname_fits_docker_dns_with_real_run_ids(self):
        key = branch_key('codex/' + 'x' * 200)
        version = 'a' * 12 + '-' + '9' * 20 + '-' + '9' * 6
        name = server.container_name(key, version)
        self.assertLessEqual(len(name), 63)
        self.assertRegex(name, r'^[a-z0-9-]+$')

    def test_privileged_request_is_bounded_and_has_no_extra_fields(self):
        request = dict(action='deploy', branch=encode_branch('feature/test'), commit='a'*40, run_id='100', attempt='1')
        self.assertEqual(server.parse_request(json.dumps(request)), request)
        for bad in [dict(request, shell='whoami'), dict(request, action='shell'), dict(request, commit='../../etc/passwd'), dict(request, run_id=10)]:
            with self.assertRaises(ValueError):
                server.parse_request(json.dumps(bad))
        with self.assertRaises(ValueError):
            server.parse_request(' ' * 2049)

    def test_colliding_slugs_have_separate_hosts(self):
        self.assertNotEqual(branch_key('feature/a'), branch_key('feature-a'))
        self.assertNotEqual(branch_key('Feature-a'), branch_key('feature-a'))
        self.assertLessEqual(len(branch_key('x' * 240)), 63)

    def test_unusual_branch_names_cannot_inject_shell_or_routes(self):
        for branch in ['feature/blog', 'fix/手机', 'feature/$(whoami)', 'feature/";evil']:
            token = encode_branch(branch)
            self.assertRegex(token, r'^[A-Za-z0-9_-]+$')
            self.assertEqual(decode_branch(token), branch)
            key = branch_key(branch)
            self.assertRegex(key, r'^up-[a-z0-9-]+$')
            self.assertNotIn(branch + ';', server.nginx_text(key + '.example.com', key))
        for token in ['../bad', 'a;whoami', '']:
            with self.assertRaises(ValueError):
                decode_branch(token)

    def test_route_generation_rejects_injection(self):
        for host, container in [('x;return 200', 'up-test'), ('x.example.com', 'x;bad')]:
            with self.assertRaises(ValueError):
                server.nginx_text(host, container)

    def test_generations_order_retries_and_new_runs(self):
        self.assertLess(server.generation('10', '1'), server.generation('10', '2'))
        self.assertLess(server.generation('10', '2'), server.generation('11', '1'))
        with self.assertRaises(ValueError):
            server.generation('1;whoami', '1')
