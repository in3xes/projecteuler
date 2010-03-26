import pdb

def merge_sort(a, b):
    c = []
    xa = xb = 0

    while 1:
        a_xa = a[xa]
        b_xb = b[xb]
        if a_xa < b_xb:
            c.append(a_xa)
            xa += 1
        else:
            c.append(b_xb)
            xb += 1

        if xa == len(a):
            c.extend(b[xb:])
            return c
        
        elif xb == len(b):
            c.extend(a[xa:])
            return c

def rmerge_sort(a, b):
    c = []
    xa = xb = 0

    while 1:
        a_xa = a[xa]
        b_xb = b[xb]
        if a_xa < b_xb:
            c.append(a_xa)
            xa += 1
        else:
            c.append(b_xb)
            xb += 1

        if xa == len(a):
            c.extend(b[xb:])
            return c
        
        elif xb == len(b):
            c.extend(a[xa:])
            return c

def insertion_sort(a):

    sl = a[:]

    for i in xrange(1, len(a)):
        key = sl[i]
        for j in xrange(i - 1, -1, -1):
            if key > sl[j]:
                break

            sl[j+1] = sl[j]
            sl[j] = key

    return sl
            
    
    
a1 = range(1,200,20)
b1 = range(4,150,30)
li = [3,326,1,36,7,06,71,2]

a = [4]
b = [3]
def main():
    print "Merge Sort"
    c=merge_sort(a,b)
    print "a =", a
    print "b =", b
    print "c =", c
    print
    print "Insertion Sort"
    lis = insertion_sort(li)
    print "Insertion sort of", li, "is =", lis
    
if __name__ == "__main__":
    main()
    
            
        
