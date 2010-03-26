
from primegenerator1 import *

primes = []
for i in primes_generator(5000):
    primes.append(i)

#print primes

# n**2 + a*n + b, |a| < 1000, |b| < 1000 
# for max consecutive values of n,
# starting from n = 0.
# b has to be prime

def check_next_primes(a, b, primes, n):
    eqn_value = n**2 + a*n + b
    #print "eqnval = ", eqn_value
    if eqn_value in primes:
        return True
    else:
        return False
    

number_of_primes = 2
max_number = 0
a_final = 0
b_final = 0

for p1 in primes:
    #print "p1=", p1, "p2=", p2
    if p1>1000:
        break
    number_of_primes = 2
    b = p1
    for p2 in primes:
        number_of_primes = 2
        a = p2 - p1 - 1
        if abs(a) > 1000:
            break
              
        #print "a=", a, "b=", b
        n = 2
    
        while 1:
            if check_next_primes(a, b, primes, n) == True:
                number_of_primes += 1
                n += 1
            else:
                break

        if number_of_primes > max_number:
                max_number = number_of_primes
                a_final = a
                b_final = b

print "a=", a_final
print "b=", b_final
print "Consecutive primes=", max_number
        
    
    

