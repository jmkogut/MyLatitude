from app import *

def Exit( code=0, msg="Exiting application..." ):
    ''' Forcibly quit execution. '''
    print " -- %s" % ( msg )

    __import__('sys').exit( code )

class Do:
    def __init__(s, Fn): s.fn = Fn
    def With ( s, src ):  return map( s.fn.__call__, src )

def db_init():
    db.create_all()
    exit()

