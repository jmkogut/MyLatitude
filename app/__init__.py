from flask import *

# =-=-=-
# App init
global application
application = Flask( __name__ )
application.config.from_pyfile('config.py')
application.debug =  application.config.get('DEBUG')

# =-=-=-
# Init DB
db = SQLAlchemy()
db.app = application
db.init_app( application )

from models import Update

# Site init, load views & models.
import views, handlers
