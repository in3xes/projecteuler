
# The decimal number, 585 = 1001001001_(2) (binary), is palindromic in
# both bases.

# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not
# include leading zeros.)

import number_op

def check_double_palindrome(dec_no):
    if dec_no != number_op.reverse(dec_no):
        return False
    
    bin_no = number_op.convert_to_binary(dec_no)

    if bin_no != number_op.reverse(bin_no):
        return False

    print dec_no, ":", bin_no

    return True
    

sum = 0
for dec_no in xrange(1, 1000000, 2):
    if check_double_palindrome(dec_no):
        sum += dec_no

print "The sum is:", sum
