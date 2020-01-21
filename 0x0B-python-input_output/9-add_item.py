#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

arguments = argv[1:]
lst = load_from_json_file('add_item.json')
lst = []
save_to_json_file(lst + arguments, 'add_item.json')
