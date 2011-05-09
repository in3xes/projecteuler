#!/usr/bin/env python
#

#
#Brute force for now

from cipher import text

schar = [x for x in range(97, 123)]
bchar = [x for x in range(65, 91)]
space = [32]
allowed = []
allowed.append(schar)
allowed.append(bchar)
allowed.append(space)

red = [x for x in range(1, 31)]
red.append(127)

def xor(txt, key):
    ans = []
    if len(key) != 3:
        print "Something wrong with key"
        return ans

    for i, c in enumerate(txt):
        k = i % 3
        p = c ^ key[k]
        ans.append(p)
        if p in red:
            ans = []
            return ans

    return ans


def ptxt(txt):
    ans = ''
    fans = 0
    for x in txt:
        ans += (chr(x))
        fans += x

    return ans, fans



if __name__ == '__main__':
    for x in schar:
        for y in schar:
            for z in schar:
                key = [x, y, z]
                ptext = xor(text, key)
                if len(ptext) != 0:
                    ans, fans = ptxt(ptext)
                    print key
                    print ans
                    print fans

        
