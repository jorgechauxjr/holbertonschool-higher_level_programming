#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[replace if n == search else n for n in my_list]
# ternary operator and list comprehension in python
