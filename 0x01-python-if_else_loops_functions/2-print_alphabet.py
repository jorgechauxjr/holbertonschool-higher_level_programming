#!/usr/bin/python3
for i in range(97, 123):
    print("{:c}" .format(i), end="")
# "end" on print func avoid \n and allow me to append in the same line
# 97 and 123 are the ascii code for the letters
