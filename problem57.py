#!/usr/bin/env python
#Simple math
#

def next_num(n, d):
    return d, (d * 2) + n


root = lambda n, d:(n+d, d)


if __name__ == '__main__':
    n = 1
    d = 2
    count = 2
    ans = 0
    while count < 1000:
        n, d = next_num(n, d)
        an, ad = root(n, d)
        if len(str(an)) > len(str(ad)):
            ans += 1
            print an, ad, ans, count
        count += 1

    print ans
