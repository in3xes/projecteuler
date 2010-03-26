from math import *
import sys
primes_list, i = [2], 3
lim = int (sys.argv[1])
while len(primes_list) < lim:
    (lambda x:  True not in map ( lambda elem: x%elem == 0, [li for li in primes_list if li <= sqrt(x)] )  and primes_list.append(x) )(i)
    i = i + 2
print primes_list[len(primes_list) - 1]



