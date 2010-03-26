import primegenerator
import sys
import pdb
import factorization

def get_distinct_primes(num, known_primes = None, factor_class = None):
    if factor_class is None:
        factors_dict = primegenerator.find_factorization_dict(num, print_value = False, primes_generated = True, primes_list = known_primes)
    else:
        factors_dict = factor_class.get_factorization_dict(num = num,
                                                           known_primes = known_primes)
        
    #print "Factorization of %d is %s" % (num, factors_dict)
    return len(factors_dict)

def main():
    try:
        dist_primes_reqd = int(sys.argv[1])
    except:
        dist_primes_reqd = 3
        
    len_reqd = dist_primes_reqd
    numbers = []
    for i in primegenerator.primes_generator(1000000):
        pass
    known_primes = primegenerator.global_primes

    factor_class = factorization.factor_wrap(known_primes = known_primes)
    

    #pdb.set_trace()
    
    for num in xrange(10, 1000000):
        distinct_primes = get_distinct_primes(num, known_primes, factor_class)
        if distinct_primes != dist_primes_reqd:
            #print distinct_primes,
            if len(numbers) == len_reqd:
                print numbers
                #break
            numbers = []
            continue
        else:
            numbers.append(num)

if __name__ == "__main__":
    main()
            
        
        
        
# Ans: [134043, ..., 134046]
