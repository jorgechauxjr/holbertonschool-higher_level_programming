#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = (number) % 10 * -1
else:
    lastDigit = number % 10

print("Last digit of {0:d} is {1:d} ".format(number, lastDigit), end="")

if lastDigit > 5:
    print("and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("and is 0".format(number, lastDigit))
else:
    print("and is less than 6 and not 0".format(number, lastDigit))
# The "end" key of print function will set the string that needs
#  to be appended when printing is done.
# ends=""allow me to append and print in the conitionals, instead of new line.
