class fibonacci:
	def __init__(self):
		self.first = 0
		self.second = 0

	def nextNum(self):
		for i in xrange(1,4):
			next = self.first + self.second
			self.first = self.second
			self.second = next
			if self.second == 0:
				self.second = 1
		return next


fibObj = fibonacci()

sum = 0
num = 0
counter = 0
while 1==1:
	#sum = sum + num
	counter += 1
	num = fibObj.nextNum()
	if num >= 1e100:
		print num, " and counter = ", counter
		break

print sum
		 
	
	



