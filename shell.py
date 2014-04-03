#!/usr/bin/env bpython

from latitude import application as app, MainMethod, db
from latitude import models
from latitude.util import abort

def Install():
    print "Installing."

__import__('os').environ['PYTHONINSPECT'] = 'True'

@MainMethod(__name__)
def BPy_Shell ():
    ''' TODO: write the helpers you mentioned in SHELL.md '''
    try:
        import readline
        import bpython
        bpython.embed( locals_={ 'app': app, 'db': db, 'models': models, install = Install }, )
    except Exception, e:
        abort( msg="Encountered an exception while loading the bpython shell.")
