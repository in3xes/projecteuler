#!/usr/bin/python

from primes import primes
from combination import combi


def primefact(num):
	pfact = []
	for p in primes:
		if p/2 > num:
			break
		elif num%p == 0:
			pfact.append(p)
		else:
			pass

	return pfact

def allpfact(num):
	fact = []
	p = 0
	while True:
		pr = primes[p]
		if pr/2 > num:
			break
		elif num%pr == 0:
			fact.append(pr)
			num = num/pr
			p = 0
		else:
			p += 1
	return fact

def allfact(number):
	af = allpfact(number)
	idx = {}
	prms, powr = [], []

	def fact(pr, pw):
		num = 1
		if len(pr) != len(pw):
			return 1
		for pos, n in enumerate(pr):
			num = num*(n**pw[pos])

		return num
	
	for n in af:
		if n in idx:
			idx[n] += 1
		else:
			idx[n] = 1

	for x in idx:
		prms.append(x)
		powr.append(idx[x])

	ary = []
	ary = combi(powr, pos=0, Ans=[])
	ans = []
	for x in ary:
		f = fact(prms, x)
		if f not in ans and f < number:
			ans.append(f)

	ans.sort()
	return ans


if __name__ == '__main__':
	f = primefact(1111111111111111111111111111111111)
	print f, len(f)
