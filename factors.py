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
		if a not in lst:
			lst.append(a)		
		if x not in lst:
			lst.append(x)
		fact(a/x, lst)
	else:
		if a not in lst:
			lst.append(a)
		lst.sort()
	return lst

l= []
a =144
print fact(a,l)
print len(l)


#It's not working
