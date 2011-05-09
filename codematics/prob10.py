n = 4231
#a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
a=[23]
b = 0
for x in a:
	tmp = n
	s = 0
	while tmp >0:
		tmp = tmp/x
		s += tmp
	b += s

print b
