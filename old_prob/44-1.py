##

from math import *

def P(n):
    return (0.5 * n * (3*n - 1))

def solve_diff(n, k):
    '''The two numbers are n and n+k.
    P(n) and P(n+k) are the two pentagonal numbers.
    This function solves for the equation:
    P(n+k) - P(n) = P(x)

    3x^2 - x - (3k^2 + 6nk -k) = 0'''

    D = 1 + 12*(3*k*k + 6*n*k -k)
    x = (1 + sqrt(D))/6


    return x


min_diff = 0
Pset = set([])
for n in xrange(1,100):
    print "n=", n,
    for k in xrange(1,100):
        x = solve_diff(n,k)
        #print "n+k=", n+k, "x=", x, "P(n+k)-P(n)=", P(n+k) - P(n), " P(x)=", P(x)
        Pnk = P(n+k)
        Pn = P(n)
        Pset.add(Pnk)
        Pset.add(Pn)
        Pnsum = P(n+k) + P(n)
        
        if x == int(x):
            print "n+k=", n+k, "x=", x, "P(n+k)-P(n)=", P(n+k) - P(n), " P(x)=", P(x)
            if min_diff == 0 or P(x) < min_diff:
                min_diff = P(x)
            break
    
print "The minimum difference is ", min_diff
    
    

    
    
