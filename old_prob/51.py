

import primegenerator
import math


limit = 1000000

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
    for i in xrange(1, limit):
        func(i, primes_test, 7)
