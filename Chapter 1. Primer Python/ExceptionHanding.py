import math
import collections

def sqrt(x): 
    if not isinstance(x, (int, float)): 
        raise TypeError('x must be numeric.')
    elif x < 0: 
        raise ValueError('x cannot be negative.')

    # do the real work here...
    return math.sqrt(x)


def sum(values): 
    if not isinstance(values, collections.Iterable): 
        raise TypeError('parameter must be an interable type.')
    
    total = 0 
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric.')
        
        total = total + v
    
    return total 
    

x = 10, y = 20
try:
    ratio = x / y 
except ZeroDivisionError: 
    print('we cannot divide by 0.')
