
import math

def find_solutions(p):
    count = 0
    for a in xrange(1, p/3):
        for b in xrange(a, (p-a)/2):
            c = math.sqrt(a**2 + b**2)
            #print "a=", a, "b=", b, "c=", c
            if b>c:
                break
            if c == (p - a - b):
                #print "a=", a, "b=", b, "c=", a**2+b**2
                count += 1

    return count


def main():
    max_sol = 0
    p_max = 0
    for i in xrange(12,1000):
        num_sol = find_solutions(i)
        #print "Solutions for", i, " is:", num_sol
        if num_sol > max_sol:
            max_sol = num_sol
            p_max = i

    print "Perimeter=", p_max
    print "Number of solutions=", max_sol

#print find_solutions(120)
main()
