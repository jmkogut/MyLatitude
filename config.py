''' Configuration settings for this web application. '''
import os
env = lambda k: lambda e: os.environ[k] if k in os.environ else e

# Title
APP_NAME  = "MyLatitude"

# DB
DB_USER   = "latitude"
DB_PASS   = None
DB_URI    = env('LATITUDE_DATABASE')("sqlite:///:memory:")
SQLALCHEMY_DATABASE_URI = DB_URI

# Host info, defaults to an env var
HOST_NAME = env('LATITUDE_HOST')(__import__('socket').gethostname())


# Enable debugging while in development
DEBUG     = True

SECRET_KEY = "secret"
# Project root dir
BASE_PATH = os.getcwd()
STATIC_FOLDER = BASE_PATH + '/static'

global GOOGLE_CLIENT_ID
global GOOGLE_CLIENT_SECRET
global REDIRECT_URI

GOOGLE_CLIENT_ID     = env('GOOGLE_CLIENT_ID')("")
GOOGLE_CLIENT_SECRET = env('GOOGLE_CLIENT_SECRET')("")
REDIRECT_URI         = "http://{0}/oauth".format(HOST_NAME)
