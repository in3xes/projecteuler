
import sys

def factors_uniq(n):

    counter = 0
    
    factors_list = [1] * n
    for i in xrange(2, n):
        counter += 1
        if factors_list[i] != 1:
            continue
        
        for mul in xrange(i, n, i):
            counter += 1
            try:
                factors_list[mul].append(i)
            except:
                factors_list[mul] = [i]

    print "Total number of iterations: %d" % (counter)
    return factors_list



def coprimes_num(num, factors_list):
    '''Returns number of coprimes of given num, also given a list of
    factors for each number upto num.'''
    
    #print "Num is", num
    factors_list_trunc = factors_list[:num+1]
    factors_num = factors_list[num]
    #print "Factors_num is %s, flist is %s" % (factors_num, [1 for x, y in enumerate(factors_list_trunc) if x > 1 and False not in map(lambda z: z not in factors_list[num], y)])
    
    n = sum([1 for x, y in enumerate(factors_list_trunc) if x > 1 and False not in map(lambda z: z not in factors_list[num], y)]) + 1


    #print "Number of coprimes of %d is %d" % (num, n)
    #print "n/phi(n) = %f" % (num * 1.0/ n)

    np_ratio = num * 1.0 / n
    
    return [num, np_ratio]   




def main(limit):
    factors_list = factors_uniq(limit)
    for i,j in enumerate(factors_list):
        pass
        #print "For %d, factors list is %s" % (i, j)
        
    max_np = [1, 1]
    for num in xrange(2,limit):
        np = coprimes_num(num, factors_list)
        if np[1] > max_np[1]:
            max_np = np

    print "Max np is %s" % (max_np)
        


if __name__ == "__main__":
    main(int(sys.argv[1]))
#try:
#main(int(sys.argv[1]))

#except:
#main(1000)

