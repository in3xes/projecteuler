#!/usr/bin/python

import factors
import primefactors

def sum_fact(b):
	l = factors.fact(b)
	l.pop(len(l)-1)
	lp = primefactors.primefact(b)
	sum = 0
	sump = 0
	for x in l:
		sum = sum + x
	for x in lp:
		sump = sump + x

	print "Prime factors are", lp, "\nSum: ", sump
  	print "All factors are: ", l, "\nSum: ", sum


sum_fact(123456)


#Incomplete
