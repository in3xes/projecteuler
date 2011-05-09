#!/usr/bin/python

import primefactors as pf
import math as m


def isabun(num):
	factors = pf.allfact(num)
	s = sum(factors)
	if s > num:
		return True
	else:
		return False

if __name__ == '__main__':
	l = []
	for x in xrange(1, 28214):
		print x
		if isabun(x):
			l.append(x)

	ans = [n for n in xrange(1, 28214)]
	length = len(l)
	for i,x in enumerate(l):
		for j in xrange(i, length):
			print x, l[j]
			v = x + l[j]
			if v in ans:
				ans.remove(v)



	print ans
	print sum(ans)
		

		

