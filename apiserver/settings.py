# encoding: utf-8

"""
This module contains the default values for all settings.

If you add settings here remember to:
    * add groups in an alphabetical order if it is possible;
    * group similar settings without leaving blank lines;
    * add some comments on your settings;
    * remove them when they became unnecessary.
"""

import os

VAGRANT = os.path.exists('/vagrant')

# This is a project-wide debug mode switch.
# Please never use another variable to switch debug mode.
DEBUG = False
if VAGRANT and not os.environ.get('NODEBUG', False):
    DEBUG = True

LIVE = not DEBUG

# Default server port to listen on.
SERVER_PORT = 5000

# Local file system paths
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates')
print TEMPLATES_PATH
MEDIA_PATH = "/data/apiserver/media" if not VAGRANT else os.path.abspath(os.path.join(PROJECT_PATH, "media"))
FILES_PATH = '/data/apiserver/files' if not VAGRANT else os.path.abspath(os.path.join(MEDIA_PATH, 'files'))
PUBLIC_FILES_PATH = os.path.abspath(os.path.join(FILES_PATH, 'public'))
PRIVATE_FILES_PATH = os.path.abspath(os.path.join(FILES_PATH, 'private'))
