
import sys

def perm_1(l, c = 0):
    if len(l) > 1:
        for c_pass in xrange(0, len(l)):
            print "Removing %s from %s, and" % (l[c_pass], l),
            print "Passing %s with c_pass=%d" % (l[0:c] + l[c+1:],
                                                 c_pass)
                                                 
            
            perm(l[0:c]+l[c+1:], c_pass)

    else:
        try:
            print "1st:", l[c]
        except:
            print sys.exc_info()
        try:
            print "Rest:", l[0:c]+l[c+1:]
            print "List:", l
        except:
            print sys.exc_info()
        
# abc: a, bc -> ab, c -> abc
#            -> ac, b -> acb
#      b, ac -> ba, c -> bac
#            -> bc, a -> bca
#      c, ab -> ca, b -> cab
#            -> cb, a -> cba

def perm_2(l, lorg = None):
    for c in xrange(0, len(l)):
        elem = l[c]
        rest = l[0:c] + l[c+1:]
        print "Elem is %s, rest is %s" % (elem, rest)
        perm(rest)
        
# abc: a, bc -> ab, c -> abc
#            -> ac, b -> acb
#      b, ac -> ba, c -> bac
#            -> bc, a -> bca
#      c, ab -> ca, b -> cab
#            -> cb, a -> cba

def perm(l, lorg = [], recur_level = 0, permutations = []):

    
    if len(l) == 0:
        #print "Zero!, lorg = %s " % (lorg)
        permutations.append(lorg)
        
    for c in xrange(0, len(l)):
                
        elem = l[c]
        rest = l[0:c] + l[c+1:]
        #lorg.append(elem)
        #print "Elem is %s, rest is %s, lorg is %s, level is %s" % (elem, rest, lorg + [elem], recur_level)

        perm(rest, lorg + [elem], recur_level + 1, permutations)

    #print "Returning from level %s... " % (recur_level)

    return permutations

def main(l):
    #for c in perm(l):
    #    print "Permutation = %s" % (c)
    permutations = perm(l)
    
    print "The permutations are %s" % (permutations)
    print "The number of permutations of %d elements is %d." % (len(l), len(permutations))
l = ['a','b','c','d','e', 'f']

if __name__ == "__main__":
    main(l)

    
    
