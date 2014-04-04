''' Utility methods for the rest of the project, shit that just didn't fit anywhere else. '''

import os
import sys


def log(m, *ins):
    str = " -- " + m.format(*ins)
    print str
    return str

log._ = lambda l: map(log, l)

def abort(code=0, msg="Exiting application..."):
    ''' Forcibly quit execution. '''
    log(msg)
    sys.exit(code)


def printcwd():
    ''' Prints the current working directory. '''
    log("Current dir is == {0}", os.getcwd())


def singleton(cls):
    ''' Only allows one instance of a cls to exist at a time. '''
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


def Blank(msg=None):
    ''' Placeholder method. '''
    log(msg)

    return None


@singleton
class SysPath(object):

    def __init__(self):
        ''' Class will check if it's been ran before, '''
        self.fixed = False

    def status(self):
        ''' Prints a short message whether or not this has been ran prior. '''
        log("SysPath %s" % ("has been fixed" if self.fixed else
            "has not been fixed yet"))

    def append(self, above=None):
        ''' Appends the dir above args['above'] or os.getcwd() to sys.path
            if no arg is provided.
        '''
        self.status()

        if above:
            log("Supplied with %s" % above)

            _dir = os.path.dirname(above)
            add = os.path.abspath(_dir+'/../')
        else:
            add = os.getcwd()
            log("Using CWD of %s for sys.path"%add)

        log("Adding %s to sys.path"%add)
        sys.path.insert(0, add)

        self.fixed = True


def Install():
    raise NotImplementedError("TODO: Write an installer helper.")


def MainMethod(name, test='__main__'):
    ''' Only execute the provided func if __name__ eq args['test'], default is __main__. Otherwise it will just leave the function alone as if nothing happened.

        Usage:
            @MainRun(__name__)
            def method():
                print "only auto exec'd if name is main."

        This basically replaces the whole 'if __name == '__main__' shuffle.
    '''
    Pass = (name == test)

    pos = "@Main decorator applied to a method and passed test, -> fn()."
    neg = "@Main failed __name__ test, fn will not be called"
    log(pos if Pass else neg)

    def dec(fn):
        wrap = lambda do: do() if Pass else log("Condition failed")
        return wrap(fn)

    return dec if Pass else lambda fn: lambda: fn()
