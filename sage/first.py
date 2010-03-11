import sys
from sage.all import *
if len(sys.argv) != 2:
    print "Usage: %s <n>"%sys.argv[0]
    print "Outputs the prime factorization of n."
    sys.exit(1)

print type(["000"])

print factor(sage_eval(sys.argv[1]))

