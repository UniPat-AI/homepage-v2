#!/usr/bin/python3
"""Forced SSH key command: only upload files or invoke the no-argument preview API."""
import os
import sys

command = os.environ.get('SSH_ORIGINAL_COMMAND', '').strip()
if command == 'preview':
    os.execv('/usr/bin/sudo', ['sudo', '-n', '/usr/local/sbin/unipat-preview'])
elif command in ('/usr/libexec/openssh/sftp-server', 'internal-sftp', 'sftp'):
    os.execv('/usr/libexec/openssh/sftp-server', ['sftp-server'])
else:
    sys.exit('This deployment key permits only SFTP and the preview API')
