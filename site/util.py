from pretty import pprint

def Exit( code=0, msg="Exiting application..." ):
    ''' Forcibly quit execution. '''
    print " -- %s" % ( msg )

    __import__('sys').exit( code )

class Do:
    def __init__(s, Fn): s.fn = Fn
    def With ( s, src ):  return map( s.fn.__call__, src )

if __name__ is '__main__':
    di  = dict( zip( map(chr,range(97,122)), range(97,113) ) )
    get = lambda i: di[i]

    print 'value of "a" is %s' % get('a')

    k = di.keys()[5:10]
    print "key subset is %s" % ", ".join(k)

    fin = map(str, map(get, k) )

    print 'fin is %s' % ", ".join(fin)
    print 'vals for teh keys are :: %s' % (  ", ".join(fin) )

    res = Do( get ).With( k )
    pprint(  'res %s'% (res) )
