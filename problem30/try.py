def fac(num):
	ans=1
	for x in range(num):
		ans=ans*(x+1)
	return ans	
a=[1]
a_fin=[]
no=5
buff=[]
req=4
for x in range(1,req+1):
	pos=-1
	a_fin=a*x*fac(x)
	for y in range(x*fac(x)):
		if y%fac(x)==0:
			pos=pos+1
		if y%x==0:
			a_fin[y+pos]=x
		if x==2:
			buff=a_fin
	if x > 2:
		buffindex=0
		buff=buff*x
		for y in range(x*fac(x)):
			if a_fin[y]==1:
				a_fin[y]=buff[buffindex]
				buffindex = buffindex + 1
	if x ==req:
		for y in range(len(a_fin)):
			if y%x==0:
				print a_fin[y:y+x]
#	print a_fin,len(a_fin)
	buff=a_fin
