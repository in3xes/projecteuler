#!/usr/bin/env python

# problem ##39


def gentriple(m, n):
    if n <= m:
        return None
    else:
        return n*n - m*m, 2*m*n, n*n + m*m


if __name__ == '__main__':

    triplets = []
    m, n = 0, 0
    while True:
        while True:
            tri = gentriple(m, n)
            if tri is not None:
                triplets.append(tri)
            n += 1
            if 2 * n * (m + n) > 1000:
                n = 1
                break
        m += 1
        if 2 * n * (m + n) > 1000:
            break

        sol = {}
    for x in triplets:
        s = sum(x)
        if s in sol:
            sol[s] += 1
        else:
            sol[s] = 1

    m = 0
    for x in sol:
        if sol[x] > m:
            m = sol[x]
            
    print m, sol[120], triplets
            
