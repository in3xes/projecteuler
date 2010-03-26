
'''Inlcudes functions to generate primes.'''


#import pdb
import sys
import math
import cPickle

try:
    LIMIT = int(sys.argv[2])
except:
    LIMIT = 121

# Eratosthenes Sieve
global_primes = [1]
global_primes_len = len(global_primes)

def primes_generator(limit = LIMIT):
    
    global global_primes, global_primes_len
    

    if global_primes is None or global_primes_len < limit+1:
        global_primes = [1 for i in xrange(0, limit + 1)]
        global_primes_len = len(global_primes)
    
        yield 2
        global_primes = mark_numbers(global_primes, 2)
        yield 3
        global_primes = mark_numbers(global_primes, 3)

        for n in xrange(6, (global_primes_len/6) * 6 + 6, 6):

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
    while prime_multiple < global_primes_len:
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
            prime_factorization_list[prime] += 1

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


    

def main():
    for n in primes_generator():
        print n, ", ",

def main_factorize(num, number_of_factors_input):
    while find_factorization((num*(num+1))/2, print_value = False) < number_of_factors_input:
        num += 1
        pass
    find_factorization((num*(num+1))/2, print_value = True)

def dump_primes(file_name = "globalprimes"):
    global global_primes
    f = open(file_name, 'w')
    cPickle.dump(global_primes, f)
    f.close()
    

if __name__ == "__main__":
    for n in primes_generator(10000000):
        pass
    dump_primes()
    
    num = 1000
    try:
        number_of_factors_input = int(sys.argv[1])
    except:
        number_of_factors_input = 50

    print "Done.."
    main_factorize(num, number_of_factors_input)
    
