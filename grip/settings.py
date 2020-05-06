"""\
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Override them using command-line arguments or with a settings_local.py in
this directory or in ~/.grip/settings.py instead.
"""
import os


HOST = os.getenv('GRIP_HOST', 'localhost')
PORT = os.getenv('GRIP_PORT', 6419)
DEBUG = os.getenv('GRIP_DEBUG', False)
DEBUG_GRIP = os.getenv('GRIP_DEBUG_GRIP', False)
CACHE_DIRECTORY = os.getenv('GRIP_CACHE_DIRECTORY', 'cache-{version}')
AUTOREFRESH = os.getenv('GRIP_AUTOREFRESH', True)
QUIET = os.getenv('GRIP_QUIET', False)


# Note: For security concerns, please don't save your GitHub password in your
# local settings.py. Use a personal access token instead:
# https://github.com/settings/tokens/new?scopes=
USERNAME = os.getenv('GRIP_USERNAME')
PASSWORD = os.getenv('GRIP_PASSWORD')


# Custom GitHub API
API_URL = os.getenv('GRIP_API_URL')


# Custom styles
STYLE_URLS = []
