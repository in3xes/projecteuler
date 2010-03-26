
import primegenerator
import math

def next_prime(primes_sieve):
    for num, val in enumerate(primes_sieve):
        if val == 1:
            yield num

        else:
            continue
        
def get_possible_squares(num):
    ten_power = 0
    allowed = [0, 2, 8]
    val = 0
    ten_multiple = 0
    while 1:
        for i in allowed:
            val = num - (ten_multiple+i)
            if val < 1:
                raise StopIteration
            yield val
                        
        ten_multiple += 10

def check_valid_prime(num, primes):
    for prime_test in get_possible_squares(num):
        if primes[prime_test] == 1:     # Number is a prime
            sq_test = math.sqrt((num - prime_test) / 2.0)
            if sq_test == int(sq_test):
                #print "The number is:", num, "=", prime_test, "+ 2 *", sq_test, "^2"
                return True

    print "False! For number", num
    return False

def main():
    known_primes = []
    for prime in primegenerator.primes_generator(limit = 10000):
        pass

    gp = primegenerator.global_primes
    num = 9
    while 1:
        if gp[num] == 0:
            if check_valid_prime(num,gp) == False:
                print "False encountered for", num
                ## if input() == 0:
                break
        num += 2
    
if __name__ == "__main__":
    main()
