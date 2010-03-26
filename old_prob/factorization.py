
import sys

class factor_wrap:
    
    def __init__(self, known_primes, factorizations = {}):
        self.known_primes = known_primes
        self.factorizations = factorizations
        
    def get_factorization_dict(self, num, known_primes = None):
        if known_primes is None:
            known_primes = self.known_primes
        
        number = num
        factors_dict = {}
        
        for prime, val in enumerate(known_primes):
            if val != 1 or prime < 2:
                continue
            
            if number == 1:
                #print "Number = 1, breaking..."
                self.factorizations[num] = factors_dict
                return factors_dict
            
            if number in self.factorizations: # Already done sometime before

                #print "Keys %s for %d:" % (self.factorizations[number], number)

                for key in self.factorizations[number].keys():

                    #print "factors_dict[%d] = %d + %d" % (key, factors_dict.get(key, 0), self.factorizations[number][key])

                    factors_dict[key] = factors_dict.get(key, 0) + self.factorizations[number][key] # Add exponent to already existing, or 1

                #############################################################################
                #     print "key=", key, "factors_dict", factors_dict                       #
                # print "%d Exists! Breaking... %s" % (number, self.factorizations[number]) #
                #############################################################################
                self.factorizations[num] = factors_dict
                
                return factors_dict

            else:
                while number % prime == 0:
                    number /= prime
                    factors_dict[prime] = factors_dict.get(prime, 0) + 1

        #print "Breaking main,,, Number is prime. Factors_dict=%s, num=%d" %(factors_dict, num)
        
        factors_dict={num:1}
        self.factorizations[num] = factors_dict
        return factors_dict



def main(limit):
    import primegenerator
    for i in primegenerator.primes_generator(limit/2):
        pass
    p = primegenerator.global_primes
    
    f1 = factor_wrap(p)
    for i in xrange(1, limit):
        print "%d is %s" % (i, f1.get_factorization_dict(i))

    #print "Factorizations are:"
    #print f1.factorizations
    return f1

if __name__ == "__main__":
    try:
        f2=main(int(sys.argv[1]))
        
    except:
        f2=main(1000)
    
