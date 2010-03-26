

import primegenerator
import math

def br_no(x):
    return x*x;

def bl_no(x, br):
    return br - x + 1

def ul_no(x, br):
    return bl_no(x, br) - x + 1

def ur_no(x, br):
    return ul_no(x, br) - x + 1

def all_no(x):
    br = br_no(x)
    bl = bl_no(x, br)
    ul = ul_no(x, br)
    ur = ur_no(x, br)
    #print "br_no=", br
    #print "bl_no=", bl
    #print "ul_no=", ul
    #print "ur_no=", ur

    return [br, bl, ul, ur]

#for i in primegenerator.primes_generator(limit = 600000000):
#    pass

def is_prime(x):
    for i in xrange(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

#primes = primegenerator.global_primes


diag_ratio = 1
r_diag = []
l_diag = []

for sq_size in xrange(3, 500000000, 2):
    all_no_list = all_no(sq_size)
    r_diag.extend([all_no_list[0], all_no_list[2]])
    l_diag.extend([all_no_list[1], all_no_list[3]])


    diag = r_diag + l_diag

    diag_prime = [is_prime(x) for x in diag]
    diag_ratio = diag_prime.count(1) * 1.0 / (len(diag) + 1)
    min_sq_size = sq_size

    print "The square size is:", sq_size
    if diag_ratio <= 0.105:
        print "The square size is:", min_sq_size
        print "The diagonal elements are:", diag
        print "The diagonal prime ratio is:", diag_ratio

    if diag_ratio < 0.1:
        break
        
    #print "l_diag is:", sorted(l_diag)

print "The minimum square size is:", min_sq_size
print "The diagonal elements are:", diag
print "The diagonal prime ratio is:", diag_ratio
