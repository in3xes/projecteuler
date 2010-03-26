
import math

def get_ten_power(numerator, denominator):
    '''Gets the power of ten required to make
    numerator>denominator.'''
    
    if numerator != denominator:
        try:
            power = int(math.log10(denominator/numerator) + 1)
            return power
            
        except:
            return 0

    else:
        return 0

        
def get_remainders(numerator, denominator):
    numerator_modified = numerator * 10**get_ten_power(numerator, denominator)
    remainder = numerator_modified % denominator
    #print remainder
    return remainder

def main(d):
    ten_num = 10**get_ten_power(1, d)
    remainders = [ten_num % d]
    while 1:
        remainders.append(get_remainders(remainders[-1], d))
        if remainders.count(remainders[-1]) > 1:
            break

    return len(remainders)

max_len = 0
max_d = 0
for d in xrange(1, 1000):
    rem_len = main(d)
    if rem_len > max_len:
        max_len = rem_len
        max_d = d

print "Maximum recurring length=", max_len
print "Number having this=", max_d


        
    
    
    
    
    
