
import primegenerator

def rotate_num(num):
    str_num = str(num)
    num_len = len(str_num)
    for index in xrange(0, num_len):
        yield str_num
        digit = str_num[0]
        str_num = str_num[1:]
        str_num += digit


def check_prime_digits(num_str):
    primes = ['1', '3', '7', '9']
    #print "num is:", num_str
    if len(num_str) > 1:
        for digit in num_str:
            if digit not in primes:
                #print "False!"
                return False
    return True


limit = 1000000
circular_primes = []
known_primes = []

for prime in primegenerator.primes_generator(limit):
    known_primes.append(str(prime))

print "Done.."
#print "Known primes are:", len(known_primes)
for prime in known_primes:
    check = 1
    for rotated in rotate_num(prime):
        if check_prime_digits(rotated) == False:
            check = 0
            break
        
        if rotated not in known_primes:
            check = 0
            break
    if check == 1:
        circular_primes.append(prime)
        print prime,",",

print
print "Length=", len(circular_primes)
        
        
        
        
