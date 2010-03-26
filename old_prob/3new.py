
import math
import sys
import pdb

primes_list = []
globalPrime = 2
def modPrimes(x):
	global globalPrime
	return globalPrime % x

## def nextPrime(current_prime):
## 	global globalPrime
## 	while 1==1:
## 		globalPrime = current_prime
## 		if 0 not in map(modPrimes, primes_list):
## 			if globalPrime != 2:
## 				globalPrime = globalPrime + 2
## 			else:
## 				globalPrime = globalPrime + 1
## 			primes_list.append(current_prime)
## 			return current_prime
			
## 		current_prime = current_prime + 2

def possiblePrimes(limit):

    yield 2
    yield 3
    
    num = 6
    while 1:
        yield num - 1
        yield num + 1
        num += 6
	if num>=limit:
		return

def nextPrime(limit = 100000):
    global_primes = []
    while 1:

        for num in possiblePrimes(limit):
	    # print "num=", num
		
            if num>=limit:
                    return
	    #pdb.set_trace()
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


prime_factorization = []

def main(num, prime_divisor):
	#print "The prime divisor is:", prime_divisor
	while 1:
		if num % prime_divisor == 0:
			if prime_divisor not in prime_factorization[0::2]:
				prime_factorization.append(prime_divisor)
				prime_factorization.append(0)

			prime_factorization[len(prime_factorization) - 1] = \
									prime_factorization[len(prime_factorization)-1] + 1

			#print num
			#print prime_factorization
			num = num / prime_divisor

		else :
			return num	


def printFactorization(orgNum):
	print orgNum, " is: "

	for counter in range(0, len(prime_factorization)):
		i = prime_factorization[counter]
		# pdb.set_trace()

		if counter == len(prime_factorization) - 1:
			print "^", i

		elif counter%2 != 0:
			print "^" , i, " * ",
		else:
			print i,

	factors_powers = []
	for c, elem in enumerate(prime_factorization):
		if c % 2 == 1:
			factors_powers.append(elem)
			
	print "Number of factors = ", reduce(lambda x,y: (x+1) * (y+1), factors_powers)
	#print nextPrime(globalPrime)

current_prime = globalPrime
num = orgNum = int (sys.argv[1])
#num = orgNum = 40
#num = orgNum =123456789012345678901234567890

#while num != 1:
## for pp in possiblePrimes(100):
## 	print pp,
## for i in range(1,10):
## 	num = main(num)


for i in nextPrime():
	num = main(num, i)
	#print i
	if num == 1:
		break
printFactorization(orgNum)

# Now the new number is the original number / small primes^exponents
# n = n/pfactors
# This new number should be accepted if it is prime, or
#				     if it is a prime number^exponent
# To find this, consider the number as 'n'.
# p ^ x = n
# => x log p = log n
# => p = pow(10, (log n)/x)
# => if pow(10,(log n )/x) is prime, then accept
# This to be iterated from x=1 to x such that pow(10,(log n)/x) < prime_divisor
# At this condition, break 
#	
## Repeat the process with the next smallest prime number




