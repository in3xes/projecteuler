#The fours pantagonal nos we are looking for are b-a , a , b , a +b in the
#same sequence.
#We will fix the value of b-a ( symbolically b_a) to some pantagonal no
# and then try to find a, such that b_a + a is pentagonal. If so we will
# check whether b + a is pentagonal or not. Considering the fact that the
# difference between P(n) and P(n+1) is 3n+1
from math import *

j = 1
m = 1
while j != 0:
    b_a = 1/2*m*(3*m-1)
    n = floor((b_a - 1)/3) # to find the upper limit for this m
    #[ m n]
    #keyboard
    for i in xrange(m+1,n):
        a = 1/2*i*(3*i-1)
        b = b_a+a
        p = 1/6*(sqrt(24*b+1)+1) #Check for pantagonal no
        c = 0;
        if floor(p) == p:
            c = a+b
            q = 1/6*(sqrt(24*c+1)+1) #Check for pantagonal no
            if floor(q)== q:
                X = [ a,b]
                print "Match! X= %s" (X)

                exit
    m = m +1
