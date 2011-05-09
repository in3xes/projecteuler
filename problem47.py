#!/usr/bin/env python

#
#Normal bruteforce checking
#should be easy

import primefactors as pf
import math as m
from primes import primes

def afdict(number):
    idx = {}
    factors = pf.allpfact(number)
    for n in factors:
        if n in idx:
            idx[n] += 1
        else:
            idx[n] = 1

    return idx

def colloid(dict1, dict2):
    if len(dict1) > len(dict2):
        for x in dict2:
            if x in dict1:
                if dict1[x] == dict2[x]:
                    return True
    else:
        for x in dict1:
            if x in dict2:
                if dict1[x] == dict2[x]:
                    return True
    return False
                
                

def isnotequal(num1, num2, aim):
    afd1, afd2 = afdict(num1), afdict(num2)
    if len(afd1) != aim or len(afd2) != aim:
        return False
    if colloid(afd1, afd2):
        return False
    else:
        return True

def main():
    count = 0
    aim = 4
    number = 2
    while True:
        print number
        if isnotequal(number, number + 1, aim) and isnotequal(number, number+2, aim) and isnotequal(number+1, number+2, aim):
            if isnotequal(number, number + 3, aim) and isnotequal(number+1, number+3, aim) and isnotequal(number+2, number+3, aim):
                print afdict(number), afdict(number+1), afdict(number+2), afdict(number+3)
                break
        number += 1

    return number
        
        
    
if __name__ == '__main__':
    print main()

