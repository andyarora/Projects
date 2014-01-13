# Find PI to the Nth Digit

import math

digits = raw_input("Enter number of digits to show pi: ")

print "{0:.{digits}f}".format(math.pi, digits = digits)