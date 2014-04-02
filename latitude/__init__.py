from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from latitude.util import log, SysPath, MainMethod
SysPath().append(above=__file__)

def app_init(cfg='../config.py'):
    ''' Initialises the flask app. '''
    log("POLLING SYSPATH")
    SysPath().status()

    app        = Flask( __name__ )
    app.config.from_pyfile(cfg)
    app.debug  =  app.config.get('DEBUG')
    return app

#if not PATH_FIXED:
#    log("Path should be fixed now why is it broken.")

application = app_init()
db = SQLAlchemy( application )


from models   import Update
from views    import *
from handlers import *
