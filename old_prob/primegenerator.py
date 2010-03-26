
'''Includes functions to generate primes.'''


import pdb
import sys
import math

if __name__ == "__main__":
    try:
        LIMIT = int(sys.argv[1])
    except:
        LIMIT = 121

# Eratosthenes Sieve
global_primes = [1]
def primes_generator(limit = 5):
    
    global global_primes

    #print "limit=", limit
    if global_primes is None or len(global_primes) < limit+1:
        global_primes = [1 for i in xrange(0, limit + 1)]
    
        yield 2
        global_primes = mark_numbers(global_primes, 2)
        yield 3
        global_primes = mark_numbers(global_primes, 3)

        for n in xrange(6, (len(global_primes)/6) * 6 + 6, 6):

            try:
                if global_primes[n-1] == 1:
                    yield n-1
                    global_primes = mark_numbers(global_primes, n-1)
            except:
                pass

            try:
                if global_primes[n+1] == 1:
                    yield n+1
                    global_primes = mark_numbers(global_primes, n+1)
            except:
                pass

    else:
        for num, is_prime in enumerate(global_primes):
            #print "Yes!"
            if is_prime == 1 and num>1:
                #print "Yielding:", num
                yield num
        

        
def check_prime(number, num_list):
    if num_list[number] == 0:
        return False
    
def mark_numbers(num_list, prime):
    prime_multiple = prime * 2
    while prime_multiple < len(num_list):
        num_list[prime_multiple] = 0
        prime_multiple += prime
    return num_list


def find_factorization(number, print_value = True):
    prime_factorization_list = [0 for i in xrange(0, number / 2 + 1)]
    number_of_factors = 1
    number_org = number
    for prime in primes_generator(number / 2 + 1):
        while number % prime == 0:
            number /= prime
            try:
                prime_factorization_list[prime] += 1
            except IndexError:
                print prime
                print "Number of factors=1"

    for prime, exponent in enumerate(prime_factorization_list):
        if exponent>0:
            if print_value is True:
                print prime, "^", exponent, "*",
            number_of_factors *= exponent + 1

    if print_value is True:
        print
        print "Number=", number_org
        print "Number of factors= ", number_of_factors

    return number_of_factors


def find_factorization_dict(number, print_value = True, primes_generated = False, primes_list = None):
    prime_factorization_list = [0 for i in xrange(0, number + 1)]
    number_of_factors = 1
    number_org = number
    factors_dict = {}


    if primes_generated == False:
        for prime in primes_generator(number / 2 + 1):
            while number % prime == 0:
                number /= prime
                try:
                    prime_factorization_list[prime] += 1
                except IndexError:
                    # print prime
                    # print "Number of factors=1"
                    pass

    else:
        for prime, val in enumerate(primes_list):
            if prime < 2:
                continue
            
            if prime > (number):
                #print "Breaking for number %d at %d and val=%d" % (number, prime, val)
                break
            if val == 1:
                while number % prime == 0:
                    #print "Yes, for number %d at %d" % (number, prime)
                    number /= prime
                    try:
                        prime_factorization_list[prime] += 1
                    except IndexError:
                        #print sys.exc_info()
                        pass
        
                
        
    for prime, exponent in enumerate(prime_factorization_list):
        if exponent>0:
            # if print_value is True:
            #     print prime, "^", exponent, "*",
            number_of_factors *= exponent + 1
            factors_dict[prime] = factors_dict.get(prime, 0) + exponent # Store powers
            #print ("factors_dict[%d] = %d" % (prime, factors_dict[prime]))

    # if print_value is True:
    #     print
    #     print "Number=", number_org
    #     print "Number of factors= ", number_of_factors

    return factors_dict
    
def get_primes(limit):
    for i in primes_generator(limit):
        pass

    return global_primes

def main():
    for n in primes_generator():
        print n, ", ",

if __name__ == "__main__":
    for n in primes_generator(10000):
        pass

    num = 100
    while find_factorization((num*(num+1))/2, print_value = False) < 500:
        num += 1
        pass
    find_factorization((num*(num+1))/2, print_value = True)
    
