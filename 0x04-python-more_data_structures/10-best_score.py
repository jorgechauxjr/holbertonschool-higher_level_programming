#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_key_value = max(a_dictionary)
        return (max_key_value)
