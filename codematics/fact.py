import math as m
b = m.factorial(2515)
count = 0
for x in str(b):
	if x == '0':
		count += 1

print count
