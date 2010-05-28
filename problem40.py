#!/usr/bin/python

strin = ""
val = 1
while(len(strin) < 1000000):
    strin = strin + str(val)
    val = val + 1

ans = 1
for x in range(0, 7):
    ans = ans*int(strin[pow(10, x) - 1])

print ans
    
