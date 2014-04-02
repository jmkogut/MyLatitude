#!/usr/bin/env bpython

from latitude import application as app, MainMethod, db
from latitude import models
from latitude.util import abort

__import__('os').environ['PYTHONINSPECT'] = 'True'

@MainMethod(__name__)
def BPy_Shell ():
    try:
        import readline
        import bpython
        bpython.embed( locals_={ 'app': app, 'db': db, 'models': models }, )
    except Exception, e:
        abort( msg="Encountered an exception while loading the bpython shell.")
