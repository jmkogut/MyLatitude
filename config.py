#  =  TITLE  =
APP_NAME  = "MyLatitude"

# DB configuration
DB_USER   = "latitude"
DB_PASS   = None
DB_URI    = "sqlite:///:memory:"
SQLALCHEMY_DATABASE_URI = DB_URI

# Networking info
HOST_NAME = "live.chex.io"

# Enable debugging while in development
DEBUG     = True

# Project root director
BASE_PATH = __import__('os').getcwd()
