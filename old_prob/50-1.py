
def sum_primes(primes):
    s = 0
    for x,y in enumerate(primes):
        if y==1:
            s += x
            if s > 1000000:
                print "x=%s, y=%s, s=%s" % (x,y,s)
                break
    return s
            
import primegenerator

def get_primes(primes):
    primes_list = []
    for x,y in enumerate(primes):
        if y==1:
            primes_list.append(x)
    return primes_list

def main(primes, primes_list):
    #print primes_list
    len1 = len(primes_list)
    #print "length is ", len1
    for cons in xrange(len1/100, 0, -1):
        #print "Trying for %d consecutive numbers.." % (cons)
        # All solutions of the equation:
        # y - x = cons

        for x in xrange(0, len1):
            y = x + cons
            if y > len1:
                break
            
            sum_cons = sum(primes_list[x:y])

            try:
                if primes[sum_cons] == 1:
                    ####################################
                    # for numbers in primes_list[x:y]: #
                    #     print "%d + " % (numbers),   #
                    #                                  #
                    # print                            #
                    ####################################
                        
                    print "x = %d, y = %d : %s" % (x, y, sum_cons)
                    return
            except:
                break

for i in primegenerator.primes_generator(1000000):
    pass

primes = primegenerator.global_primes
primes_list = get_primes(primes)
primes_list = primes_list[2:]


if __name__ == "__main__":
    
    main(primes, primes_list)


