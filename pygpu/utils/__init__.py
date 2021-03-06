
__name__ = 'pygpu.utils'
__author__ = 'Calle Lejdfors <calle.lejdfors@cs.lth.se>'

def all(f, xs, initial):
    return reduce(lambda a,b: a and b, map(f, xs), initial)

def any(f, xs):
    return reduce(lambda a,b: a or b, map(f, xs), False)
    
