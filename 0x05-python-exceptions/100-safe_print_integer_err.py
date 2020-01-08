#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error_name:
        print('Exception: {}\n'.format(error_name), file=stderr)
        return False
    return True
