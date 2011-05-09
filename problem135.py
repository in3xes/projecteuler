#!/usr/bin/env python

"""Project Euler, problem 135

Given the positive integers, x, y, and z, are consecutive terms of an
arithmetic progression, the least value of the positive integer, n, for which
the equation, x**2 - y**2 - z**2 = n, has exactly two solutions is n = 27:

34**2 - 27**2 - 20**2 = 12**2 - 9**2 - 6**2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
"""

"""
x**2 - y**2 - z**2 = n
y = z + d
x = z + 2 * d
d > 0
z > 0
(z + 2 d) ** 2 - (z + d) ** 2 - z ** 2 = n
(z**2 + 4dz + 4d**2) - (z**2 + 2dz + d**2) - z**2 = n
z**2 + 4dz + 4d**2 -z**2 - 2dz - d**2 - z**2 = n
-z**2 + 2dz + 3d**2 - n = 0
a = -1
b = 2d
c = 3d**2 - n
z = (-b +/- sqrt(b**2-4ac)) / 2a
z = (-2d +/- sqrt(4d**2+4(3d**2-n))) / -2
z = (-2d +/- sqrt(4d**2+12d**2-4n))) / -2
z = (-2d +/- sqrt(16d**2-4n))) / -2
z = (-2d +/- 2 sqrt(4d**2 - n)) / -2
z = (-d +/-  sqrt(4d**2 - n)) / -1
z = d +/- sqrt(4d**2 - n)
4d**2 - n >= 0
n <= 4d**2
4d**2 - n is a perfect square
"""

def main():
    limit = 1000000
    counts = limit * [0]
    for d in range(1, limit / 4 + 1):
        d24 = d ** 2 * 4
        if d24 < limit:
            start = 1
            counts[d24] += 1
        else:
            start = int((d24 - limit) ** 0.5)
        if start < 1:
            start = 1
        for root in xrange(start, 2 * d):
            n = d24 - root ** 2
            if n <= 0:
                break
            if n < limit:
                z = root + d
                y = z + d
                x = y + d
                #print "n", n, "d", d, "root", root, "x", x, "y", y, "z", z
                #assert x**2 - y**2 - z**2 == n
                counts[n] += 1
                if d > root:
                    z = d - root
                    y = z + d
                    x = y + d
                    #print "n", n, "d", d, "root", root, "x", x, "y", y, "z", z
                    #assert x**2 - y**2 - z**2 == n
                    counts[n] += 1
    total = 0
    assert counts[0] == 0
    for val in counts:
        if val == 10:
            total += 1
    print total

if __name__ == "__main__":
    main()
