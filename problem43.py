#!/usr/bin/env python
#

from perm import perm

nums = [x for x in range(0, 10)]
divs = [2, 3, 5, 7, 11, 13, 17]

def retnum(l):
    if len(l) != 3:
        print 'Something wrong'
        return 1
    return l[0]*100 + l[1]*10 + l[2]

def yes(lst):
    ans = True
    for x in range(1, 8):
        if retnum(lst[x:x+3]) % divs[x-1] == 0:
            pass
        else:
            ans = False
            break

    return ans

def check():
    count = 0
    print nums
    p = perm(nums, [], 0, [])
    print len(p)
    for x in p:
        if x[0] != 0:
            if yes(x):
                count += 1
                print x
    return count


if __name__ == '__main__':
    print yes([1,4,0,6,3,5,7,2,8,9])
    print check()
    

                  
        
    
