#!/usr/bin/env python

# Problem #45:


def t(idx):
    return (idx * (idx + 1))/2

def p(idx):
    return (idx * (3 * idx - 1))/2

def h(idx):
    return (idx * (2 * idx  - 1))


t_s = []
p_s = []
h_s = []

pidx = 1
tidx = 1

count = 0
for x in range(1, 30000):
    num_h = h(x)
    h_s.append(num_h)
    while True:
        num_t = t(tidx)
        t_s.append(num_t)
        if num_t in h_s:
            while True:
                num_p = p(pidx)
                p_s.append(num_p)
                if num_p in h_s:
                    print x, pidx, tidx
                    count = count + 1
                if num_p > num_h:
                        break
                pidx = pidx + 1
        tidx = tidx + 1
        if num_t > num_h:
            break
    if count == 3:
        break
    print len(h_s), len(p_s), len(t_s), x

print pidx - 1, tidx - 2, h_s[-1], p_s[-2], t_s[-2]

            
            
