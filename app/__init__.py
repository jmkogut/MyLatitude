
from app import App

# init app
application = App( 'config' )

# load views && models
from site import views, models

# set debug option
application.debug = conf.DEBUG
global application

