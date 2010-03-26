
power_list = []
a_limit = 100
b_limit = 100

for a in xrange(2, a_limit + 1):
    for b in xrange(2, b_limit + 1):
        power = a**b
        if power not in power_list:
            power_list.append(power)

print len(power_list)
        
