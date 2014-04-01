
from flask import *
import os, sys

config = __import__('config')

# =-=-=- app init
global application
application = Flask( config.APP_NAME )
application.config.from_object( 'config' )

# database init
db = SQLAlchemy( application )

# Site init, load views & models.
from app import views, models

@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

application.debug = conf.DEBUG
