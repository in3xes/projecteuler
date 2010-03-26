from math import *

# To find the largest prime factor of a very large number

# Number = ( Largest prime factor ^ exponent ) * Product of other prime numbers and their exponents

class primes:

	def __init__(self):
		self.current_prime = 2
		self.primes_list = []

	def isPrime(self, number):
		root = int (sqrt(number))
		
		next_prime = 2

		while next_prime < root:
			next_prime = getNextPrime(next_prime)

	def getNextPrime(self, curr_prime = current_prime):
		if current_prime not in self.primes_list:
			self.primes_list.append(curr_prime)

		if current_prime == 2:
			self.primes_list.append(3)
			return 3

		else:
			test_number = curr_prime
			while 1==1:

				test_number = test_number + 2
				check = 1
				
				#print "Now beginning..."	
				for smaller_prime in self.primes_list:
					#print "test_number = ", test_number
					#print "smaller_prime = ", smaller_prime
					if test_number % smaller_prime == 0:
						check = 0
						break

				if check == 1:
					current_prime = test_number
					return test_number



	def execModule(self, number = 1):
		for i in range (1,5):
			print getNextPrime()
			

P = primes()
num = 2
counter = 0
#while counter < 5:
	#print "For number:", num
#	num = P.getNextPrime(num)
#	print num
#	counter = counter + 1

P.execModule()

