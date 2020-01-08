#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for elements in my_list[0:x]:
            print("{:d}".format(elements), end="")
            counter += 1
    except (IndexError, ValueError, TypeError):
        print("")
    finally:
        print()
        return counter
