
import sys

known_coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Powers generated is the representation
# of the simple binomial expansion of
# (1 - x**val)**-1


# Uses binomial theorem to obtain coefficient of the desired sum in
# the expansion of the multiplied terms of allowed values

def multiply_lists(l1, l2, max_val = None):
    if max_val is None:
        final_list = [0] * (len(l1) + len(l2))
    else:
        final_list = [0] * (max_val + 1)

    for t1, po1 in enumerate(l1):
        
        if po1 >= 0:
            for t2, po2 in enumerate(l2):
                if po2 >= 0:
                    try:
                        final_list[t1+t2] += po1*po2
                    except:
                        continue
    return final_list

def multiply_lists_optimized(l1, l2, max_val):

    final_list = [0] * (max_val + 1)

    for t1, po1 in enumerate(l1):
        for t2, po2 in enumerate(l2):
            try:
                final_list[t1+t2] += po1*po2
            except:
                continue
    return final_list

def print_series(l):
    for t, po in enumerate(l):
        if po != 0:
            if t == 0:
                print "1 +",
            elif po > 1:
                print "%dx^%d +" %(po, t),
            else:
                print "x^%d +" %(t),

def get_list(power, limit):
    list_series = [0]*(limit+1)
    for i in xrange(0, limit+1, power):
        list_series[i] = 1
    return list_series

    
def get_final_series(known_values, final_sum):

    interm_list = [0]*final_sum
    interm_list[0] = 1

    for val in known_values:
        val_list = get_list(val, final_sum)
        interm_list = (multiply_lists_optimized (val_list, interm_list, final_sum))
        
    return interm_list
        

def get_ways_to_sum(known_values, final_sum):
    fl = get_final_series(known_values, final_sum)
    print "The number of ways to achieve the sum of", final_sum, "from the set"
    print known_values, "is:", fl[final_sum]
    
if __name__ == "__main__":
    try:
        final_sum = int(sys.argv[1])
    except:
        final_sum = 200
    get_ways_to_sum(known_coins, final_sum)
    

