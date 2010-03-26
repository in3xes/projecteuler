LOWER = 1
UPPER = 100

sqsum = sum(map(lambda x: x*x, range(LOWER, UPPER + 1)))
sumsq = sum(range(LOWER, UPPER + 1)) ** 2

print "sqsum = ", sqsum
print "sumsq = ", sumsq
print "Diff = ", (sumsq - sqsum)
