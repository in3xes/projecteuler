import sys
import pprint

lst = [1] * 10
for i in [2, 3, 5, 7]:
    j = i
    cp = [x for x in range(1, len(lst)) if x % j != 0]
    
    for elem in cp:
        if j < elem:
            
            try:
                lst[elem].append(j)
            except:
                lst[elem] = [1, j]
        
    #cp = filter(lambda x: x%j != 0, range(1,len(lst)))
    print "For %d, coprimes are %s" % (j, cp)

print "The final lst is:"

pprint.pprint(lst)

    
    



    
