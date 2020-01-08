#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for elements in my_list[0:x]:
        try:
            print("{:d}".format(elements), end="")
            counter += 1
        except (IndexError, ValueError, TypeError):
            pass
    print()
    return counter
