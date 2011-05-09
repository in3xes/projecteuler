
s = 0
c = 0
for x in range(1, 2097152):
	n = x
	count = 0
	while n>0:
		if n%2:
			count += 1
		n = n/2
	if count == 11:
		s = s+x
		c += 1
		print x
print s
print c
