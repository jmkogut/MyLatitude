#!/usr/bin/python

import os
import sys

def FixPath( above=None ):
    if above:
        print("Supplied with %s" % above)

        dir = os.path.dirname(above)
        add = os.path.abspath(dir+'/../')
    else:
        add = os.getcwd()
        print("Using CWD of %s for sys.path"%add)

    print("Adding %s to sys.path"%add)
    sys.path.insert(0, add)

FixPath()#above=__file__)
