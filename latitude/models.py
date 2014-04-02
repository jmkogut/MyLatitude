''' Table definitions, our data structures. '''

from latitude import db
from latitude.util import *

from sqlalchemy import *


class Update(db.Model):
    ''' This model represents a location update. '''

    __tablename__ = 'updates'

    COLUMNS = ['username', 'password', 'latitude', 'longitude',
               'accuracy', 'loc_timestamp', 'req_timestamp',
               'offset', 'device']

    id            = db.Column('id', Integer, primary_key=True)
    username      = db.Column('username',      String(30))
    latitude      = db.Column('latitude',      String(30))
    longitude     = db.Column('longitude',     String(30))
    accuracy      = db.Column('accuracy',      String(30))
    loc_timestamp = db.Column('loc_timestamp', DateTime())
    req_timestamp = db.Column('req_timestamp', DateTime())
    offset        = db.Column('offset',        String(30))
    device        = db.Column('device',        String(30))

    def __repr__(self):
        return '<Update %s - %s>' % (self.username, self.id)

    @classmethod
    def from_user(cls, **kwa):
        ''' Retrieves a user model from a column. '''
        pass

    @classmethod
    def create(cls, **cols):
        ''' Creates a update model and saves it. '''
        pass

# =-=-=-

@singleton
class Helpers(object):
    ''' A collection of related methods for working with databases. '''

    def Create(self, db, quit_after=True):
        ''' Creates all the tables / db files / whatever may be needed. '''
        db.create_all()
        (abort if quit_after else Blank)()

METHODS = Helpers()
