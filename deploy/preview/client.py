"""Stable, shell-safe preview identifiers shared by CI and the installed server."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re


def branch_key(branch):
    if not isinstance(branch, str) or not branch or len(branch.encode()) > 240 or any(ord(c) < 32 for c in branch):
        raise ValueError('Invalid branch name')
    slug = re.sub('[^a-z0-9]+', '-', branch.lower()).strip('-')[:30].rstrip('-') or 'branch'
    return 'up-' + slug + '-' + hashlib.sha256(branch.encode()).hexdigest()[:12]


def encode_branch(branch):
    branch_key(branch)
    return base64.urlsafe_b64encode(branch.encode()).decode().rstrip('=')


def decode_branch(encoded):
    if not re.fullmatch('[A-Za-z0-9_-]{1,320}', encoded):
        raise ValueError('Invalid encoded branch')
    branch = base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4)).decode()
    if encode_branch(branch) != encoded:
        raise ValueError('Non-canonical branch encoding')
    return branch


def main():
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    deleting = os.environ['GITHUB_EVENT_NAME'] == 'delete'
    branch = event['ref'] if deleting else event['workflow_run']['head_branch']
    if (deleting and event['ref_type'] != 'branch') or branch == 'main':
        raise ValueError('Preview operations only accept non-main branches')
    key = branch_key(branch)
    host = key + '.' + os.environ['PREVIEW_DOMAIN']
    values = {'key': key, 'branch_token': encode_branch(branch), 'url': 'http://' + host}
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        for name, value in values.items():
            output.write(name + '=' + value + '\n')


if __name__ == '__main__':
    main()
