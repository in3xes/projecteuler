
import math

factorials = {}
for num in xrange(0, 10):
    factorials[str(num)] = math.factorial(num)
    
numbers = []

for i in xrange(11, 100000):
    str_num = str(i)
    fact_sum = 0
    for digit in str_num:
        fact_sum += factorials[digit]
        if fact_sum > i:
            break
    if fact_sum == i:
        print i
        numbers.append(i)

print "Sum=", sum(numbers)
    
        
    
