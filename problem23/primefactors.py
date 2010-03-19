#!/usr/bin/python

import math

def primefact(a, lst=[]):
	x = 2
	while x <= int(math.sqrt(a)):
		if int(a)%int(x) == 0:
			break
		else:
			x = x+1

	if x <= math.sqrt(a):
		if x not in lst:
			lst.append(x)
		primefact(a/x, lst)
	else:
		if a not in lst:
			lst.append(a)
		lst.sort()
	return lst

if __name__ == '__main__':
	print primefact(9760197719)
