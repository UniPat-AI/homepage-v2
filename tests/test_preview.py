import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'deploy/preview'))
sys.path.insert(0, str(ROOT / 'deploy'))
from client import branch_key, encode_branch, decode_branch
spec = importlib.util.spec_from_file_location('preview_server', ROOT / 'deploy/preview/server.py')
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class PreviewTests(unittest.TestCase):
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
