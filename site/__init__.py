import config
from app import App

# init app
application = Application( cfg )

# load views && models
from site import views, models

# set debug option
application.debug = conf.DEBUG
global application

