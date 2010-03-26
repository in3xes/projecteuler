def multiply_check(a, b):
    astr = str(a)
    bstr = str(b)
    aset = set(astr)
    bset = set(bstr)

    if len(aset.intersection(bset)) != 0 or len(astr) != len(aset) or \
       len(bstr) != len(bset):
        return False

    else:
        c = a * b
        cstr = str(c)
        if '0' in cstr:
            return False
        cset = set(str(c))
        if len(aset.intersection(cset)) == 0 \
           and len(bset.intersection(cset)) == 0 \
           and len(aset) + len(bset) + len(cset) == 9 \
           and len(cset) == len(cstr):
            print a, "*", b, "=", c
            return c
        else:
            return False

def main():
    seen_products = []
    count = 0
    for a in xrange(1,100):
        if '0' in str(a):
            continue
        if a < 10:
            lower_b = 1000
            upper_b = 9999
        else:
            lower_b = 100
            upper_b = 999
            
        for b in xrange(lower_b, upper_b + 1):
            if '0' in str(b):
                continue
            m_c = multiply_check(a, b)
            if m_c:
                if m_c not in seen_products:
                    seen_products.append(m_c)
                    count += 1

    print "The products are:", seen_products
    print "The sum of the products is:", sum(seen_products)
    print "The number is:", count


if __name__ == "__main__":
    main()
