# -*- coding: cp1252 -*-
# Fibonacci Sequence - Enter a number and have the
# program generate the Fibonacci sequence to that number
# or to the Nth number

import sys

result = {}

def fib(n):
	retval = 0
	if n in result: return result[n]
	elif n <= 2:
		retval = 1
	else:
		retval = fib(n-1) + fib(n-2)
	result[n] = retval
	return retval

print fib(int(raw_input("Enter the Nth number: ")))

