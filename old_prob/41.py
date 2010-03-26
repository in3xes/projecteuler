
import primegenerator
import number_op

def main():
    known_primes = [0] * 7654322
    for i in primegenerator.primes_generator(7654321):
        known_primes[i] = 1

    print "Done."
    
    for j in xrange(7654321, 1, -1):
        str_j = str(j)
        len_j = len(str_j)
        elements_valid = [str(x) for x in xrange(1, len_j + 1)]
        check = 1
        for elem in elements_valid:
            if elem not in str_j:
                check = 0
                break
        if check == 1 and known_primes[j] == 1:
            return j
        
print main()

               


    
