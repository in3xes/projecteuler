sum=0
for i in range(3,1000,3):
	sum = sum + i
for j in range(5,1000,5):
	if j%3 != 0:
		sum = sum +j

print sum

