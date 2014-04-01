from flask import *

class App( cfg=None ):
    def __init__( self ):
        self.chk_config( conf )

        global application
        application = Flask( conf.APP_NAME )
        application.config.from_object( 'conf' )
        self._app = application

    def run( self, host=None, debug=None ):
        global application
        application = self._app
        application.run( **{
            'host':  host  if host else config.HOST_NAME,
            'debug': debug if debug else config.DEBUG
        } )

    def chk_config( self, conf ):
        if not conf:
            import sys
            print "Exiting, no config."
            sys.exit(0)
