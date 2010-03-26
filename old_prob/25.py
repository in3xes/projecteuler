import sys
class fibonacci:
	def __init__(self):
		self.first = 0
		self.second = 0
		self.count = 0

	def nextNum(self):
		for i in xrange(1,4):
			next = self.first + self.second
			self.first = self.second
			self.second = next
			self.count += 1
			if self.second == 0:
				self.second = 1
		return next


fibObj = fibonacci()

sum = 0
num = 0
counter = 0

try:
	digits = int(sys.argv[1])
except:
	digits = 100
	
while 1==1:
	#sum = sum + num
	counter += 1
	num = fibObj.nextNum()
	if num >= 10**(digits - 1):
		print num, " and counter = ", fibObj.count
		break

print sum





