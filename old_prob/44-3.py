
#The fours pantagonal nos we are looking for are b-a , a , b , a +b in the
#same sequence.
#We will fix the value of b-a ( symbolically b_a) to some pantagonal no
# and then try to find a, such that b_a + a is pentagonal. If so we will
# check whether b + a is pentagonal or not. Considering the fact that the
# difference between P(n) and P(n+1) is 3n+1
from math import *

numiter = 0
j = 1
m = 1

plist = map(lambda x: x*(3*x-1)/2, range(1,10000))

while j != 0:
    #b_a = m*(3*m-1)/2
    b_a = plist[m-1]
    n = int(floor((b_a - 1)/3)) # to find the upper limit for this m
    #[ m n]
    #keyboard
    #print "n = %d, b-a = %d, m = %d" % (n, b_a, m)
    for i in xrange(m+1,n):

        #a = i*(3*i-1)/2
        try:
            a= plist[i-1]
        except:
            pass
            #print "i=", i
        b = b_a+a
        p = (sqrt(24*b+1)+1)/6 #Check for pantagonal no
        c = 0;
        numiter += 1
        #print "m = %d, n = %d, b-a = %d, i = %d, a = %d, b = %d, iter = %d" % (m, n, b_a, i, a, b, numiter)
        if floor(p) == p:
            c = a+b
            q = (sqrt(24*c+1)+1)/6 #Check for pantagonal no
            if floor(q)== q:
                X = [a,b]
                print "Match! X= %s" % (X)

                exit
    m = m +1

    

print "m = %d, n = %d, b-a = %d, i = %d, a = %d, iter = %d" % (m, n, b_a, i, a, numiter)
