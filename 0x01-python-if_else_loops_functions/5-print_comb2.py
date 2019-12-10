#!/usr/bin/python3
for num in range(0, 100):
    if num != 99:
        print("{0:02d},".format(num), end="")
    else:
        print("{0:02d}".format(num))
# numbers can be constrained to a specific width
# {0:02d} 0 is the zero parameter of format(), in this case "num"
# {0:02d} 2 is the width of the number. "d" means decimal
# and 0 is the number that will fill the empty space.
