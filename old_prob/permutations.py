import pprint
import sys

def perm(l, lorg = [], recur_level = 0, permutations = []):
    """Returns a list containing all permutations of a given
    list.
    Each permutation is in the form of a rearranged list.
    The elements of the original list are only manipulated by
    position, and hence, the type of each element can be
    arbitrary.
    Anonymous lists are used in the passing of parameters
    so as to prevent in-place modification of the original
    list."""
    
    
    if len(l) == 0:
        permutations.append(lorg)
        
    for c in xrange(0, len(l)):
        elem = l[c]
        rest = l[0:c] + l[c+1:]

        perm(rest, lorg + [elem], recur_level + 1, permutations)

    return permutations

def iperm(l, lorg = [], recur_level = 0):
    """Iterator for permutations.
    TODO:Should be improved so that it takes fewer function calls.
    FIXME:Currently repeats levels during processing.
    
    Each permutation is in the form of a rearranged list.
    The elements of the original list are only manipulated by
    position, and hence, the type of each element can be
    arbitrary.
    Anonymous lists are used in the passing of parameters
    so as to prevent in-place modification of the original
    list."""
    
    
    if len(l) == 0:
        yield lorg
            
    for c in xrange(0, len(l)):
        elem = l[c]
        rest = l[0:c] + l[c+1:]
        for p in iperm(rest, lorg + [elem], recur_level + 1):
            #print "P is %s, recur_level is %s, l is %s" % (p, recur_level, l)
            yield p
            
        
def main(l):
    permutations = perm(l)
    pprint.pprint(permutations)
    print "The number of permutations of %s is %s." % (l, len(permutations))
    
def imain(l):
    for i in iperm(l):
        print "Permutation is %s" % (i)
            
if __name__ == "__main__":
    l = range(1,8)
    try:
        main_arg = sys.argv[1]
    except:
        main_arg = 'i';
        
    if main_arg == 'i':
        imain(l)
    else:
        main(l)
