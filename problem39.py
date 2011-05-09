#!/usr/bin/env python

#problem 39

#
#No logic, Bruteforce

def tri(x, y, z):
    if x*x == (y*y + z*z):
        return True
    else:
        return False


a = 1
lst = []
total = []
while True:
    b = a
    while True:
        c = b
        while True:
            t = [a, b, c]
            t.sort()
            if tri(t[2], t[1], t[0]):
                print t
                total.append(t)
                if t not in lst:
                    lst.append(t)
            c += 1
            if a+b+c >= 1000:
                break
        b += 1
        if a + b >= 999:
            break
    a += 1
    if a >= 998:
        break

ls = []
for x in lst:
    ls.append(sum(x))

s = {}
for x in ls:
    if x in s:
        s[x] += 1
    else:
        s[x] = 1


m = 0
v = 0
for x in s:
    if s[x] > m:
        m = s[x]
        v = x

print m, v
print lst
print ls
print s
