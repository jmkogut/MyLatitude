#!/usr/bin/env python

# -----------
# Load globals for the interactive session
import config
import os, sys
print "cwd is %s"%(os.getcwd(), )

from app import *

os.environ['PYTHONINSPECT'] = 'True'

#
# -----------

# -----------
# Launch ipython shell
def Session ():
    from IPythonimport import embed
    embed("IT FEELS LIKE THE FIRST TIME~")

#from IPython.terminal.ipapp import TerminalIPythonApp
#app = TerminalIPythonApp.instance()
#app.initialise( argv=[] )
#app.start()
#
# ------------

if __name__ is '__main__':
    Session()
