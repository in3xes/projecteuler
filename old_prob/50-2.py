

def main(arr1):
    print arr1
    len1 = len(arr1)

    for cons in xrange(len1, 0, -1):
        print "Trying for %d consecutive numbers.." % (cons)
        # All solutions of the equation:
        # y - x = cons

        for x in xrange(0, len1):
            y = x + cons
            if y > len1:
                break
            print "x = %d, y = %d : %s" % (x, y, sum(arr1[x:y]))
            
        



if __name__ == "__main__":
    main(range(1,10))
