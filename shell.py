#!/usr/bin/env python

# -----------
# Load globals for the interactive session
import os
print "$CWD == %s" % ( os.getcwd() )

os.environ['PYTHONINSPECT'] = 'True'

from app import *
#
# -----------

# -----------
# Launch shell
def BPy_Shell ():
    import bpython
    bpython.embed( locals=globals(), )
    import readline


if __name__ is '__main__':
    BPy_Shell()
