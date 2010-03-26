# What 12-digit number do you form by concatenating the three terms in
# this sequence?

import permutations
import primegenerator
from listop import *

def create_and_check(n, primes, break_num = 3):
    """Checks whether break_num number of
    distinct permutations of the given number
    are prime.

    By default, break_num is 3."""

    prime_num = 0
    primes_found = []
    nl = ntol(n)

    len_n = len(nl)
    
    for np in uniq(permutations.iperm(nl)):
        np_conv = lton(np)
        if len(str(np_conv)) != len_n:
            continue
        
        #print "np_conv is %s" % (np_conv)
        if primes[np_conv] == 1:
            prime_num += 1
            primes_found.append(np_conv)

        if prime_num == break_num:
            return sorted(primes_found)

    return None
            
def check_set(n, primes, break_num = 3):
    """Check whether there are break_num number
    of permutations of n which are primes, with
    the same common difference.

    The common difference must end with a 0 because
    two other numbers are required to be prime,
    and any number other than zero would result in
    at least one number becoming even."""



    if primes[n] == 0:
        return None
    
    sn = set(str(n))

    for diff in xrange(1000, 4500, 10):
        n1 = n + diff
        n2 = n1 + diff
        if n2 > 9999:
            return None

        if primes[n1] == 1 and set(str(n1)) == sn:
            if primes[n2] == 1 and set(str(n2)) == sn:
                return [[n, n1, n2], diff]

    return None

def main():
    for i in primegenerator.primes_generator(10000):
        pass
    primes = primegenerator.global_primes

    count_success = 0
    for i in xrange(1003,9999):
        result = check_set(i, primes)
        if result is not None:
            print "The first number is %s, result is %s with common difference %s" % (i, result[0], result[1])
            count_success += 1
            if count_success == 2:
                break


if __name__ == "__main__":
    main()

##############################
# Answer: [1487, 4817, 8147] #
#         [2969, 6299, 9629] #
##############################
