#!/usr/bin/env python

#Problem ## 50

#
#Lazymethod, Import all the primess less than million
#and do rest of the work

##
##Not working, Wrong algo

from primes import primes

def isprime(num):
    if num in primes:
        return True
    else:
        return False

def main():

    ans = 0
    for i, x in enumerate(primes):
        fi = open('f', 'a+')
        fi.write(str(x)+'\n')
        tprimes = primes[i+1:]
        s = x
        l = 0
        a = []
        for y in tprimes:
            s += y
            l += 1
            a.append(y)
            if s > 10 ** 6:
                break
            if isprime(s):
                if l > ans:
                    ans = l
                    fi.write(str(ans)+'|'+str(s)+'|ans\n')
        fi.close()
    fi = open('f', 'a+')
    fi.write(str(ans+1))
    fi.close()
    return ans+1

if __name__ == "__main__":
    main()

