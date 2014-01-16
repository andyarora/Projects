# Prime Factorization - Have the user enter a number
# and find all Prime Factors (if there are any) and
# display them.

import sys

n = int(raw_input("enter your number: "))
result = set()

#algorithm to find prime factors - start with 2 and if % is 0, work with the quotient
if n < 2:
    print "enter a number greater than 1"
    sys.exit(1)

factor = 2
while n > 1:
    if n % factor == 0: 
        result.add(factor)
        while n % factor == 0:
            n = n/factor
    factor = factor + 1

print result
