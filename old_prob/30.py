
def check_sum_powers(min_limit, max_limit, power):
    sum_numbers = 0
    for num in xrange(min_limit, max_limit+1):
        num_str = str(num)
        if sum([int(digit)**power for digit in num_str]) == num:
            print num_str
            sum_numbers += num
    return sum_numbers

sum_numbers = check_sum_powers(2, 200000, 5)
print "Sum=", sum_numbers
