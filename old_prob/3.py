# To find the largest prime factor of a composite number
# If composite => The largest prime is max. = Number / 2

# Find the prime factorization of the number
# Find the smallest primes which divide the number, and the maximum exponents
# At the same time, divide the resulting number by

import math
import sys

primes_list = []
globalPrime = 2
def modPrimes(x):
	global globalPrime
	return globalPrime % x

def nextPrime(current_prime):
	global globalPrime
	while 1==1:
		globalPrime = current_prime
		if 0 not in map(modPrimes, primes_list):
			if globalPrime != 2:
				globalPrime = globalPrime + 2
			else:
				globalPrime = globalPrime + 1
			primes_list.append(current_prime)
			return current_prime
			
		current_prime = current_prime + 2



prime_factorization = []

def main(num):
	prime_divisor = nextPrime(globalPrime)
	#print "The prime divisor is:", prime_divisor
	while 1==1:
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

		if counter == len(prime_factorization) - 1:
			print "^", i

		elif counter%2 != 0:
			print "^" , i, " * ",
		else:
			print i,
	
	#print nextPrime(globalPrime)

current_prime = globalPrime
num = orgNum = int (sys.argv[1])
#num = orgNum = 40
#num = orgNum =123456789012345678901234567890

while num != 1:
	num = main(num)

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




