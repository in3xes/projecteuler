#!/usr/bin/python

def primefact(a, lst):
	x = 2
	while x < a:
		if a%x == 0:
#			print x
			break
		else:
			x = x+1

	if x <= a/2:
		if x not in lst:
			lst.append(x)
		primefact(a/x, lst)
	else:
		if a not in lst:
			lst.append(a)
		lst.sort()
	return lst

l= []
print primefact(12,l)

