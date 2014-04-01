
from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

# =-=-=-=- OS PATH MODS =-=-=-
import os, sys

config = __import__('config')
print "Initialising [ %s ]" % ( config.APP_NAME, )

# =-=-=- app init
global application
application = Flask( config.APP_NAME )
application.config.from_object( 'config' )
application.debug = config.DEBUG

# database init
db = SQLAlchemy( application )

# Site init, load views & models.
from app import views, models

@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

