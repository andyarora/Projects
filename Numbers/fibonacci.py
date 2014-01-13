# -*- coding: cp1252 -*-
# Fibonacci Sequence - Enter a number and have the
# program generate the Fibonacci sequence to that number
# or to the Nth number

import sys

n = int(raw_input("Enter the Nth number: "))

attempts = 0

while n < 2:
	n = int(raw_input("Enter a number greater than 2: "))
	attempts = attempts + 1
	if attempts > 3:
		sys.exit(1)

retval = [0,1]

for x in range(2,n):
	retval.append(retval[x-1] + retval[x-2])

print retval