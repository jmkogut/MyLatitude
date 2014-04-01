#!/usr/bin/env python

# = = = = = = = = = = = = = = = = =
# Exec only if file called directly
if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, os.path.abspath('./') )

    print "APP_NAME is %s" % ( __import__('config').APP_NAME, )

    # =-=-=-=-=-=-=-
    # Run the testing wwwsrv

    from app import *

