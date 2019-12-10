#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
        if i == ord('q') or i == ord('e'):
                continue
        print(chr(i))
# ord() function receives a character and return the ascii code (integer)
'''
The "continue" statement rejects all the remaining statements
in the current iteration of the loop and moves the control
back to the top of the loop.
'''
# For that reason the 'q' and 'e' are not printed.
