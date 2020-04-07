#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    peak, number, prev = 0, 0, 0
    first = True

    if list_of_integers:
        for number in list_of_integers:
            if first is True:
                prev = number
                first = False
            else:
                if number >= prev and number >= peak:
                    peak = number
                    prev = number
                else:
                    prev = number
        return peak
    else:
        return None
