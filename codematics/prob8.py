def sum(a):
	s = 0
	for x in str(a):
		s += int(x)

	return s

c = 813008130081
while True:
	print c
	y = 123*c
	if sum(y) == 123:
		break
	c += 1

print c, c*123
