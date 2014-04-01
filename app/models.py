from app import application, db, config
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime

# Now done in config.py
# app.config.SQLALCHEMY_DATABASE_URI = config.DB_URI

class Update( db.Model ):

    COLUMNS = [ 'username',      'password',
                'latitude',      'longitude',     'accuracy',
                'loc_timestamp', 'req_timestamp',
                'offset',        'device' ]

    id = db.Column('id', Integer, primary_key=True)

    username      = db.Column('username',      String(30) )
    latitude      = db.Column('latitude',      String(30) )
    longitude     = db.Column('longitude',     String(30) )
    accuracy      = db.Column('accuracy',      String(30) )
    loc_timestamp = db.Column('loc_timestamp', DateTime() )
    req_timestamp = db.Column('req_timestamp', DateTime() )
    offset        = db.Column('offset',        String(30) )
    device        = db.Column('device',        String(30) )

    def __repr__(self):
        return '<Update %s - %s>' % (self.username, self.id)
