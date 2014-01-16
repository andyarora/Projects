"""
Binary to Decimal and Back Converter
Develop a converter to convert a decimal number to binary
or a binary number to its decimal equivalent.
"""

def dec_to_bin(a):

    retval = ""
    while a > 0:
        retval = retval + str(a%2) 
        a = a / 2
    retval = retval[::-1]
    return retval

def bin_to_dec(b):
    retval = 0
    index = 0
    for c in reversed(b):
        retval = retval + int(c) * (2 ** index)
        index += 1
    return retval

print dec_to_bin(int(raw_input("dec to bin: ")))
print bin_to_dec(raw_input("bin to dec: "))

