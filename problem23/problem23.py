#!/usr/bin/python

import factors

def sum_fact(b):
	l = factors.fact(b)
	l.pop(len(l)-1)
	sum = 0
	for x in l:
		sum = sum + x

  	print "All factors are: ", l, "\nSum: ", sum


sum_fact(123456)


#Incomplete
