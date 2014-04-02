
from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

# =-=-=- app init
global application
application = Flask( "WWW" )
application.config.from_pyfile('config.py') #from_object( 'config' )
application.debug =  application.config.get('DEBUG')

# database init
db = SQLAlchemy( application )

# Site init, load views & models.
from app import views, models
from app.handlers import *
