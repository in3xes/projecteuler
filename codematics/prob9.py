def sn1(sn):
	if sn < 0 or sn%4 == 3:
		return sn+4
	if sn%4 == 0:
		return sn/2
	if sn%4 == 1 or sn%4 == -3:
		return 3*sn +1
	if sn%4 == 2 or sn%4 == -2:
		return sn-25

def c(sn):
	count = 0
	while True:
		if sn ==0 or sn == 1:
			break
		count += 1
		sn = sn1(sn)
	return count
m = 0
mc = 0
lst = [x for x in range(1, 100000)]
for x in lst:
	print x
	sn = x
	lsn = []
	count = 0
	if x%4 == 3:
		continue
	while True:
		if sn ==0 or sn == 1 or sn in lsn:
			break
#		print sn, "SN", x
		lsn.append(sn)
		sn = sn1(sn)
		count += 1
	if mc < count:
		mc = count
		m = x


print mc*m
