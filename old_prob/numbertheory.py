def gcd(*args):
    """Returns the GCD of any number of numbers."""
    
    #print "args are:", args, " type is:", type(args)
    if len(args) < 2:
        raise TypeError('gcd expected 2 or more arguments, got 1')

    elif len(args) == 2:
        abs_args = [abs(args[0]), abs(args[1])]
        number_1 = max(abs_args)
        number_2 = min(abs_args)
        if number_2 == 0:
            return 0
        
        if (number_1 % number_2) == 0:
            return number_2

        else:
            return gcd(number_2, number_1 % number_2)
    
    else:
        number_1 = args[0]
        rest_numbers = args[1:]
        #print "Passing gcd(%d, gcd(%s))." % (number_1, rest_numbers)
        return gcd(number_1, gcd(*rest_numbers))
    
