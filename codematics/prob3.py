import primes as p
import math as m
print len(p.primes)
count = 0;
def sum(a, b):
	#suma = [m.fsum(int(x)) for x in str(a)]
	#sumb = [m.fsum(int(y)) for y in str(b)]
	#suma = sum(str(a))
	#sumb = sum(str(b))
	suma = 0
	sumb = 0
	for x in str(a):
		suma += int(x)
	for y in str(b):
		sumb += int(y)
	if suma == sumb:
		return True

for x in range(1, 1000000):
	if p.primes[x-1] > 1000000:
		break
	if x in p.primes:
		if sum(x, p.primes[x-1]):
			count += 1

print count
if __name__ == '__main__':
	print sum(234, 135)
