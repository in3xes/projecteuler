powers = []
grandtotal = 0
def fact(num):
	ans=1
	for x in range(1,num+1):
		ans=ans*x
	return ans	


for i in range(2,2540160):
        total = 0
        for j in str(i):
                total += fact(int(j))

        if total == i:
                powers.append(i)

for i in powers:
        grandtotal += i

print("powers:", powers)
print("total:", grandtotal)

