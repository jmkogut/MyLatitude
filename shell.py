#!/usr/bin/env python

# -----------
# Load globals for the interactive session
print "cwd is %s"%( __import__('os').getcwd(), )

from app import *

os.environ['PYTHONINSPECT'] = 'True'
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
#
# ------------
