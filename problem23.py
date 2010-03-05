#!/usr/bin/python

def fact(a, lst):
	x = 2
	while x < a:
		if a%x == 0:
#			print x
			break
		else:
			x = x+1

	if x <= a/2:
		lst.append(a)
		if x not in lst:
			lst.append(x)
		fact(a/x, lst)
	else:
		if a not in lst:
			lst.append(a)
		lst.sort()
	return lst

def sum_fact(b):
	l = []
	l = fact(b, l)
	l.pop(len(l)-1)
	sum = 0
	for x in l:
		sum = sum + x
		print x

	print sum

sum_fact(12)


#Incomplete
