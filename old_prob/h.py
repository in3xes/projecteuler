def move(el, from_c, to_c, temp_c):
    """Move el from from_c to to_c using temp_c as temp."""

    if len(el) == 1:
        print "Move from %d to %d." % (from_c, to_c)
        #print "%d -> %d, " % (from_c, to_c),

    else:
        # Move (n-1) elements to temp_c, and move the
        # remaining to to_c, then move the (n-1) elements
        # to to_c

        move(el[:-1], from_c, temp_c, to_c)
        move([el[-1]], from_c, to_c, temp_c)
        move(el[:-1], temp_c, to_c, from_c)
        
def number_of_moves(n):
    return n > 1 and 2*number_of_moves(n-1) + 1 or 1

el=[1,2,3,4,5,6,7]
move(el,1,2,3)
print "Number of moves:", number_of_moves(len(el))

"""
        f(n) = 2f(n-1) + 1
        f(1) = 1
        f(2) = 2 + 1 = 3
        f(3) = 2*3 + 1 = 7
        f(4) = 2*7 + 1 = 15
        f(5) = 2*15 + 1 = 31
        f(6) = 2*31 + 1 = 63

        f(n+1) = 2f(n) + 1
               = 2{2f(n-1) + 1} + 1

               = 2^2f(n-1) + 2 + 1
               = 2{2{2f(n-2) + 1}} + 1
               = 2^3f(n-2) + 2^2 + 1

               f(n) = 2f(n-1) + 1
                    = 2{2f(n-2) + 1} + 1
                    = 2^2f(n-2) + 2 + 1
                    

        f(n) = 2^n - 1
"""
