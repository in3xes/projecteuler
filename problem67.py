#!/usr/bin/env python

def f(name):
    x  = open(name)
    a = x.readline()
    b = {}
    index = 0
    while a:
        b[index] = map(int, a.split())
        a = x.readline()
        index += 1

    return b

def findmax(curr, prev):
    if len(curr) - len(prev) != 1:
        print "Error, Length doesn't match"

    m = []
    for x in range(len(curr)):
        if x == 0:
            m.append(curr[0] + prev[0])
        elif x == len(curr) - 1:
            m.append(curr[x] + prev[-1])
        else:
            m.append(max(curr[x] + prev[x-1], curr[x] + prev[x]))

    return m

if __name__ == "__main__":
    t = f('tri')
    a = findmax(t[1], t[0])
    for x in range(len(t) - 2):
        a = findmax(t[x+2], a)

    print len(a)
    print max(a)
