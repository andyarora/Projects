# Next Prime Number - Have the program find prime
# numbers until the user chooses to stop asking for
# the next one.

import sys

prime_numbers = [2]

def getnextprime(current_prime):
    x = current_prime
    while True:
        isprime = True
        x = x + 1
        for prime in prime_numbers:
            if x % prime == 0:
                isprime = False
                break
        if isprime:
            prime_numbers.append(x)
            return x

if __name__ == "__main__":
    current_prime = 2
    while True:
        user_response = raw_input("Do you want next prime [Y/N]: ")
        if user_response.lower().startswith('y'):
            print current_prime
            current_prime = getnextprime(current_prime)
        else:
            sys.exit(0)
