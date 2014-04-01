from flask import *
from util import Exit, DoWith

class App( ):
    def __init__( s ):
        print "App.init"

        s.cfg = __import__('config')
        s.opt = lambda i: getattr(s.cfg, i)

        # DEBUG PRINTS
        fmt = lambda k: '%s - %s' % (k, s.opt(k))
        # debug pprits
        print fmt('HOST_NAME')
        print fmt('APP_NAME' )

        s.application = Flask( s.opt('APP_NAME') )
        s.application.config.from_object( s.cfg )

    def run( s, **wwwArgs ):
        ''' Usage: App().run( host='0.0.0.0', debug=True ) '''
        with ['HOST_NAME', 'DEBUG'] as opts:
            Get = DoWith( s.opt )
            args = dict( zip( opts, Get(opts) ) )

            print "pretty ARGS - %s" % ( args )
            args.update( wwwArgs )

            print "pretty wwwARGS - %s" % ( args )

        s.application.run( **args )


if __name__ == '__main__':
    print "running app.py"

    app = App()

    print 'HOSTNAME is DBG::%s' % ( app.opt('HOST_NAME') )

    app.run()
