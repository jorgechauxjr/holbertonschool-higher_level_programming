#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
        print(chr(i), end="")
# ord() function receives a character and return the ascii code (integer)
# in this case receives 'a '97 and'z'122.
# The "for" will not print the last value (z) for that reason I need to add 1.
# "end" on print func avoid \n and allow me to append in the same line
# chr() receives ascii code (integer) and return the character.
