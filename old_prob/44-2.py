# Makes use of sets heavily
# Using a list instead would make this take a really long time


from math import sqrt

def P(n):
    return (n*(3*n-1)/2)

def get_p_list(n):
    p_list = []
    for i in xrange(1, n):
        p_list.append(P(i))
    return p_list

def is_pent(x):
    '''Tests if a number is pentagonal.'''
    
    try:
        n_test = (1 + sqrt(1 + 24*x))/6.0
    except:
        return False
    if n_test == int(n_test):
        return True
    return False

    

def main():
    numiter = 0
    p_list = set(get_p_list(3000))             # Generate the list of pentagonal numbers
                                        # Now, run a loop over the numbers, starting from the smallest
                                        # Then another inner loop over each number
                                        # In the inner loop, iterate over each number smaller than the number
                                        # And check if the difference equals the original number

    for diff_n in p_list:
        #print "Trying to form %d:" % (diff_n)
        for n1 in p_list:
            numiter += 1
            if n1 - diff_n in p_list:
                n2 = n1 - diff_n
                #print "n1 = %d, n2 = %d, n1 - n2 = %d" % (n1, n2, n1-n2)
                if n1 + n2 in p_list:
                        print "Match! n1 + n2 = %d" % (n1 + n2)
                        print "n1 = %d, n2 = %d, n1 - n2 = %d" % (n1, n2, n1-n2)
                        print "Number of iterations = ", numiter
                        return
        

if __name__ == "__main__":
    main()
    print "Done."
        

