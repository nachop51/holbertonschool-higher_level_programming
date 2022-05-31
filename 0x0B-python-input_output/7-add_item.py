#!/usr/bin/python3
""" Adds items to a json file """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
obj = [arg for arg in sys.argv if arg != sys.argv[0]]

try:
    data = load_from_json_file(filename)
except Exception:
    save_to_json_file(obj, filename)
else:
    for o in obj:
        data.append(o)
    save_to_json_file(data, filename)
