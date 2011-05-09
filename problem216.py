#!/usr/bin/env python
#

#using fermat test with high iterations


from isprimes import fermat


count = 0
for x in xrange(1, 5 * 10 ** 7):
    if fermat(2*(x**2) - 1, 30):
        count += 1
        print x

print count
        
        
