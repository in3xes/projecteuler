import decimal
import math

D = decimal.Decimal

def check(p, n):
    two_p = n - p
    three_p = p
    
    t = D(2**two_p + 3**three_p)
    s = D(1 + 8*t).sqrt()
    s2 = D(t).sqrt()
    # print "D(t).sqrt = ", s2
    
    if int(s % 10) != D(s % 10):
        return D('0.1')
    else:
        r = D(D('0.5') * (s - 1))
        return r

def is_triangle(num):
    if num % 2 == 1:
        return False
    num_twice = 2*num
    # num = n(n+1)/2 = 0.5 * (n**2 + n)
    sqr = int(math.sqrt(2 * num))
    #print "sqr=", sqr
    for offset in xrange(-1, 1):
        #print "sqr-offset=", (sqr-offset)
        if (sqr - offset) * (sqr - offset + 1) == num_twice:
            print "Yes!"
            return True
    

decimal.getcontext().prec = 100
print is_triangle(20)
def main():
    for n in xrange(501,503):
        for p in xrange(0, 500):
            #print "p=", p, " check=",
            c = check(p, n)
            #print c
            if int(c % 10) == D(c % 10):
                print "Yes!"
                print "p=", p, " n=", n, " c=", c
                z = raw_input()



    
        
        
        
