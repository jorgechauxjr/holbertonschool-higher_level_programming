#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
        print(chr(i), end="")
# ord() function is to take the ascii value of the character
# in this case'a'takes 97 and'z' 122.
# The "for" will not print the last value (z) foor that reason I need to add 1
# "end" on print func avoid \n and allow me to append in the same line
# chr() receivves ascii code (integer) and return the character.
