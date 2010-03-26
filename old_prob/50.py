

def sum_primes(primes):
    s = 0
    for x,y in enumerate(primes):
        if y==1:
            s += x
            if s > 1000000:
                print "x=%s, y=%s, s=%s" % (x,y,s)
                break
    return s
            
import primegenerator

def get_primes(primes):
    primes_list = []
    for x,y in enumerate(primes):
        if y==1:
            primes_list.append(x)
    return primes_list

for i in primegenerator.primes_generator(1000000):
    pass

primes = primegenerator.global_primes
primes_list = get_primes(primes[:4000])
primes_list = primes_list[2:]

for xmax in xrange(len(primes_list), 1, -1):
    sum_test = sum(primes_list[:xmax])
            
    print "The sum is %s and xmax is %s" % (sum_test, xmax)
    try:
        if primes[sum_test] == 1:
            print "The last prime is %s at %s" % (primes_list[xmax], xmax)
            print "The sum is %s" % (sum_test)
            break
    except IndexError:                  # Sum is greater than primes generated
        continue
