#!/usr/bin/env python

#
#Print all list less then [a, b, c]
#All the list of the form [x, y, z]
#such that x < a, y < b, z < c
#
#Recursive algorithm


def combi(l, pos = 0, Ans = []):
    if l not in Ans:
        Ans.append(l)
    tmp = False
    t = l[:]
    if pos < len(l):
        tmp = True
        combi(t, pos + 1, Ans)
    if tmp:
        if t[pos] > 0:
            t[pos] = t[pos] - 1
            combi(t, pos, Ans)
    return Ans
    


if __name__ == '__main__':
    test = [3, 2]
    ans = combi(test, pos=0, Ans=[])
    print ans
    print len(ans)
    test = [2, 2]
    a = combi(test, pos=0, Ans=[])
    print a
    print len(a)
