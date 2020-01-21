#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""

    line_number = 0
    with open(filename, 'r') as o_file:
        for a_line in o_file:
            line_number += 1
    return line_number
