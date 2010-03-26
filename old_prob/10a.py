
from math import *

# To find sum of all primes below 2M
import sys

def possiblePrimes(limit):

    yield 2
    yield 3
    
    num = 6
    while 1:
        yield num - 1
        yield num + 1
        num += 6

def nextPrime(limit):
    global_primes = []
    while 1:

        for num in possiblePrimes(limit):
            if num>=limit:
                    return

            check = 1
            # Now divide by existing primes
            # and check if divisible
            # print "global_primes = ", global_primes
            for prime in global_primes:
                if num % prime == 0:
                    check = 0
                    break                # Goes to next possible prime
            if check == 1:
                global_primes.append(num)
                yield num
        return
            

try:
    LIMIT=int(sys.argv[1])
except:
    LIMIT=200000
sumprimes=0
for i in nextPrime(LIMIT):
    sumprimes+=i

print "Sum is:"
print str(sumprimes)
    
        

