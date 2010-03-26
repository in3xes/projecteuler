
# By replacing the 1^(st) digit of *3, it turns out that six of the
# nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3^(rd) and 4^(th) digits of 56**3 with the same
# digit, this 5-digit number is the first example having seven primes
# among the ten generated numbers, yielding the family: 56003, 56113,
# 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the
# first member of this family, is the smallest prime with this
# property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an
# eight prime value family.


import primegenerator
import math


limit = 10000000

primes_test = primegenerator.get_primes(limit)
primes = [x for x in xrange(0, len(primes_test)) if primes_test[x] == 1]

ps = [x for x in primes if len(str(x)) > len(set(str(x)))]

    
#for num in primes:
        # Iterate over digit


def getcomposites(numarr, primes, reqd = 7):
    composite_counter = 0
    for num_test in numarr:
        if primes[num_test] == 0:
            composite_counter += 1
            if composite_counter == 11 - reqd:
                break
            #print "Composites: %d" % (composite_counter)
    if composite_counter < (11 - reqd):
        print "Yes!, For: %s" % (numarr)


def func(num, primes, reqd = 7):
    numstr = str(num)
    l = len(numstr)
    for pos1 in xrange(0, l-1):
        for pos2 in xrange(pos1 + 1, l-1):
            newstr = numstr
            numarr = repl_digits(numstr, pos1, pos2)
            getcomposites(numarr, primes, reqd)
            # newstr = newstr[:pos1] + '*' + newstr[pos1+1:pos2] + '*' + newstr[pos2 + 1:]
            # print newstr

def repl_digits(numstr, pos1, pos2):
    newstr = numstr
    #print
    numarr = []
    for digit_int in xrange(0, 10):
        digit = str(digit_int)
        newstr = newstr[:pos1] + digit + newstr[pos1+1:pos2] + digit + newstr[pos2 + 1:]
        newint = int(newstr)
        #print newint,
        numarr.append(newint)

    return numarr



    
    
    
if __name__ == "__main__":
    for i in xrange(1000000, limit):
        func(i, primes_test, 8)
