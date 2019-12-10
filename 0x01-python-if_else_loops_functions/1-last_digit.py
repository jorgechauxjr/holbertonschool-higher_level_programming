#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# The "end" key of print function will set the string that needs
#  to be appended when printing is done.
# ends=""allow me to append and print in the conitionals, instead of new line.
print("Last digit of {0:d} is ".format(number), end="")

if number < 0:
    number = number * -1

lastDigit = number % 10

if lastDigit > 5:
    print("{0:d} and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("{1:d} and is 0".format(number, lastDigit))
else:
    print("{1:d} and is less than 6 and not 0".format(number, lastDigit))
