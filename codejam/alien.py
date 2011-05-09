#!/usr/bin/env python

f = open('input.txt', 'r+')

tmp = f.readline()
tmp = tmp.split(' ')
tmp = [int(x) for x in tmp]
length, size, cases = tmp[0], tmp[1], tmp[2]
words = []

for n in range(0, size):
    words.append(f.readline()[:-1])

word = words[:]
for n in range(0, cases):
    case = f.readline()[:-1]
    pos = 0
    possible = word[:]
    x = 0
    first = True
    while x < len(case):
        if first:
            possible = word[:]
            first = False
        else:
            possible = list(words)[:]
        words = set([])
        if case[x] == '(':
            x += 1
            while case[x] != ')':
                letter = case[x]
                for w in possible:
                    if w[pos] == letter:
                        words.add(w)
                x += 1
            x += 1
        else:
            for w in possible:
                if w[pos] == case[x]:
                    words.add(w)

            x += 1
        pos += 1
        
    print "Case #" + str(n+1) + ":", len(words)
