#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file (UTF8)
    and prints it to stdout"""

    line_number = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line_number += 1
            if (nb_lines <= 0) or (nb_lines >= line_number):
                print(line, end="")
