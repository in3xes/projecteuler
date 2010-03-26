
# The fraction (49)/(98) is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe
# that (49)/(98) = (4)/(8), which is correct, is obtained by
# cancelling the 9s.

# We shall consider fractions like, (30)/(50) = (3)/(5), to be trivial
# examples.

# There are exactly four non-trivial examples of this type of
# fraction, less than one in value, and containing two digits in the
# numerator and denominator.

# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

def check_fraction(num, den):
    numstr = str(num)
    denstr = str(den)
    for i in xrange(0, 2):
        num_new = int(numstr[i])
        j = 1 - i
        den_new = int(denstr[j])
        if numstr[j] == denstr[i]:
                try:
                    if float(num_new) / den_new == float(num) / den and (num % den) != 0:
                        if len(set(numstr)) == len(numstr):
                            print "------------------------------------------"
                            print "Fraction, Original = ", num, "/", den
                            print "Fraction = ", num_new, "/", den_new
                            return True
                        else:
                            return False
                except:
                    return False

count = 0
for num in xrange(10, 100):
    for den in xrange(10, 100):
        if num > den:
            continue
        if check_fraction(num, den):
            count += 1

print "The number is:", count
