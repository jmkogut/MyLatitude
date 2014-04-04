''' Table definitions, our data structures. '''

from latitude import Base, db, engine
from latitude.util import *

from sqlalchemy import *
from sqlalchemy.orm import relationship

BACKITUDE_COLS = ['username', 'password', 'latitude', 'longitude',
                  'accuracy', 'loc_timestamp', 'req_timestamp',
                  'offset']


class Identity(Base):
    ''' User profiles. '''

    __tablename__ = 'identity'

    id                      = db.Column('id', Integer, primary_key=True)
    token                   = db.Column('token',    String(30))
    locale                  = db.Column('locale',   String(30))
    email                   = db.Column('email',    String(30))
    username                = db.Column('username', String(30))
    created                 = db.Column('created',  String(30))
    lastseen                = db.Column('seen',     String(30))

    checkins                = relationship("CheckIn", backref="user")
    config                  = relationship("Config",  backref="user")

    @classmethod
    def Create(cls, t, l, e, u, c, seen ):
        ident = Identity(token=t,
                         locale=l,
                         email=e,
                         username=u,
                         created=c,
                         lastseen=seen)
        db.session.add(ident)
        db.session.commit()
        return ident

    @classmethod
    def where(cls, **kwa):
        return Identity.query.filter_by(**kwa)

class CheckIn(Base):
    ''' This model represents a location update. '''

    __tablename__ = 'checkin'

    user_id          = db.Column(Integer, db.ForeignKey('identity.id'))

    id            = db.Column('id', Integer, primary_key=True)
    latitude      = db.Column('latitude',      String(30))
    longitude     = db.Column('longitude',     String(30))
    accuracy      = db.Column('accuracy',      String(30))
    offset        = db.Column('offset',        String(30))

    created = db.Column('loc_timestamp', DateTime())
    synced  = db.Column('req_timestamp', DateTime())

    def __repr__(self):
        return '<Checkin for %s - %s>' % (self.user.username, self.id)

    @classmethod
    def from_user(cls, **kwa):
        ''' Retrieves a user model from a column. '''
        pass

    @classmethod
    def create(cls, **cols):
        ''' Creates a update model and saves it. '''
        pass


class Config(Base):
    ''' Server-side sessions, simple key/value store. '''

    __tablename__ = 'config'

    user_id          = db.Column(Integer, db.ForeignKey('identity.id'))

    id               = db.Column('id', Integer, primary_key=True)
    key              = db.Column('key',        String(16))
    value            = db.Column('value',      String(512))


# =-=-=-

@singleton
class Helpers(object):
    ''' A collection of related methods for working with databases. '''

    def Create(self, quit_after=False):
        ''' Creates all the tables / db files / whatever may be needed. '''
        log("All tables initialised for db(`%s`)." % app.config.get('DB_URI'))
        Base.metadata.create_all(bind=engine)
        (abort if quit_after else Blank)()

    def Drop(self, quit_after=False):
        """ Drops all defined tables. """
        log("All tables dropped for db(`%s`)." % app.config.get('DB_URI'),)
        Base.metadata.drop_all(bind=engine)
        (abort if quit_after else Blank)()

    def find_user( **kwa ):
        ''' Queries for user identities.

            Usage: find_user(email='dottru@gmail.com')
                   find_user(username='admin') '''
        res = Users.query.filter( **kwa )
        log('%s results found' % res.count())
        return res

    def test_db():
        pass

METHODS = Helpers()
