
## Let the numbers be a<b<c
## => a+b - ab/1000 = 500
## => ab is a multiple of 1000
## c = 1000 - a - b

## Let c = 500
## ab should be a multiple of 1000
## a + b = 1000 - c = 500, a>=1, 2<b<499
## Start from a = 1 => b = 499
## If ab is not a factor of 1000, next a
## If ab is a factor of 1000, check if c^2 = a^2 + b^2
## If no, c' = c - 1, a = 1, b = 999 - c'
## If yes, return

import sys
counter = 0
def trip(N):
    c = int(N/2) + 1
    global counter
    
    while c > int(N/3):

        c = c - 1
        #print "c is:", c
        for a in range(1, int(N/2)):
            b = N - c - a
            if a >= b:
                break

            #print "*a = ", a, " b = ", b

            if a*b % N != 0:
                continue

            else:
                #print "True!"
                counter = counter + 1
                if (c**2 == a**2 + b**2):
                    print "a = ", a
                    print "b = ", b
                    print "c = ", c
                    return [a,b,c]

    print "No solution!"
    


print "argv is:", sys.argv[1]
try:
    l = trip(int(sys.argv[1]))
except:
    l = trip(1000)

print "triplets are:", l
print "Number of squares checked: ", str(counter)



            
