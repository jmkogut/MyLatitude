import os

from flask import Flask, g
from flask_oauth import OAuth

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from latitude.util import log, SysPath, MainMethod
from latitude.api import API
from simplejson import dumps as JSON

SysPath().append(above=__file__)


import config as conf

def app_init(cfg='../config.py'):
    ''' Initialises the flask app. '''

    app        = Flask( __name__, static_folder=os.path.abspath('static'))
    app.register_blueprint(API, url_prefix='/api')
    app.config.from_pyfile(cfg)
    app.debug      =   app.config.get('DEBUG')
    app.secret_key = app.config.get('SECRET_KEY')
    oauth = OAuth()

    '''GOOGLE_CLIENT_ID = conf.GOOGLE_CLIENT_ID
    GOOGLE_CLIENT_SECRET = conf.GOOGLE_CLIENT_SECRET
    '''

    google = oauth.remote_app('google',
      base_url='https://www.google.com/accounts/',
      authorize_url='https://accounts.google.com/o/oauth2/auth',
      request_token_url=None,
      request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email',
        'response_type': 'code'},
      access_token_url='https://accounts.google.com/o/oauth2/token',
      access_token_method='POST',
      access_token_params={'grant_type': 'authorization_code'},
      consumer_key=app.config.get('GOOGLE_CLIENT_ID'),
      consumer_secret=app.config.get('GOOGLE_CLIENT_SECRET'))

    return app, google

application, gauth = app_init()
application.auth  = gauth

engine = create_engine( application.config.get('DB_URI'), convert_unicode=True)
session = scoped_session(sessionmaker(
    autocommit=True,
    autoflush=True,
    bind=engine
))
Base = declarative_base()
Base.query = session.query_property()

db = SQLAlchemy( application )


from models   import Identity, CheckIn
from views    import *
from handlers import *
