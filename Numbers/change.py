# Change Return Program - The user enters a cost and
# then the amount of money given. The program will figure
# out the change and the number of quarters, dimes, nickels,
# pennies needed for the change.

import math

def change(cost, given, denominations):
    #check if cost and given are floats
    #check if given is less than or equal to cost

    #returns a list of tuples where first value is denomiations and second qty
    retval = []
    remainder = given - cost
    for key in sorted(denominations.keys(), reverse=True):
        required_qty = remainder // key
        right_qty = min(required_qty, denominations[key])
        if right_qty > 0:
            retval.append((key, right_qty))
            remainder = remainder - (right_qty * key)
        if remainder == 0:
            break 

    return retval, remainder

cost = float("{:.2f}".format(float(raw_input("enter the cost: "))))
given = float("{:.2f}".format(float(raw_input("enter the given: "))))
denominations = {20 : 10, 10 : 10, 5 : 10, 1 : 10, .25 : 100, 
                .05 : 100, .01 : 100}

print change(cost, given, denominations)