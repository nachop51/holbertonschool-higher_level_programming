#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None


def my_div(a, b):
    return a / b


result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len


result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
