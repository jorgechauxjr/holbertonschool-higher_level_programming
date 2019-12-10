#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n == 100:
            print("Buzz", end="")
        elif n % 3 != 0 and n % 5 != 0:
            print("{0:d} ".format(n), end="")
        elif n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz ", end="")
        elif n % 3 == 0:
            print("Fizz ", end="")
            if n % 5 == 0:
                print("Buzz ", end="")
