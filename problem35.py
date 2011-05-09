#!/usr/bin/python

a = [2]
isprime = True
for x in xrange(3, 1000000):
    isprime = True
    for y in a:
#        print x,y,x/y
        if x%y == 0:
            isprime = False
            break
    if isprime:
        a.append(x)

print a
count = 0
for x in xrange(2, 1000000):
    yes = True
    for y in range(0, len(str(x))):
        x_s = str(x)
#        l_list = []
#        l_list.append(int(x_s[y:]+x_s[:y]))
        val = int(x_s[y:]+x_s[:y])
        if val not in a:
            yes = False
            break

    if yes:
        count = count+1
#        print x

#print count
