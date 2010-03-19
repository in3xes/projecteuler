#!/usr/bin/python
import re

for x in range(10, 300):
	pattern = re.compile("0")
	if pattern.match((str(x)), len(str(x))-1 ):
		print x

