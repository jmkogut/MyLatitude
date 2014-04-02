''' Configuration settings for this web application. '''
import os
# Title
APP_NAME  = "MyLatitude"

# DB
DB_USER   = "latitude"
DB_PASS   = None
DB_URI    = "sqlite:///:memory:"
SQLALCHEMY_DATABASE_URI = DB_URI

# Host info, defaults to an env var
HOST_NAME = os.environ['APP_HOST'] or "live.chex.io"

# Enable debugging while in development
DEBUG     = True

# Project root dir
BASE_PATH = os.getcwd()
