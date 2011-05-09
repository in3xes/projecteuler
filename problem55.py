#!/usr/bin/env python

#Problem ## 55

#
## No logic required

def ispal(num):
    l = len(str(num))
    if l == 1:
        return True
    pos = l/2
    fh = int(str(num)[:pos])
    sh = str(num)[-pos:]
    sh = int(sh[::-1])
    if fh == sh:
        return True
    else:
        return False

def islyc(num):
    count = 0
    rnum = int(str(num)[::-1])
    num = num + rnum
    while count < 49:
        if ispal(num):
            return False
        rnum = int(str(num)[::-1])
        num = num + rnum
        count += 1

    return True

count = 0
for x in xrange(1, 10 ** 4):
    if islyc(x):
        count += 1


print islyc(4994)
print count
    
        

                 
        
