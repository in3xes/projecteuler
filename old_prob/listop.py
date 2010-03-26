def ntol(n):
    """Returns a list containing individual
    elements of the number."""
    
    return map(int, str(n))

def lton(l):
    """Returns the number corresponding to the
    elements of the list."""
    
    return sum([n*10**p for p,n in enumerate(l[::-1])])

def uniq(l):
    """Returns only one of each element in the list."""
    
    uniq_l = []
    for elem in l:
        if elem not in uniq_l:
            uniq_l.append(elem)

    return uniq_l
        
