#!/usr/bin/env bpython

# = = = = = = = = = = = = = = = = =
# Exec only if file called directly
if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, os.path.abspath('.') )

    # =-=-=-=-=-=-=-
    # Run the testing wwwsrv
    from app import  *

    application.run(
        host  = application.config.get('HOST_NAME'),
        debug = application.config.get('DEBUG') )
