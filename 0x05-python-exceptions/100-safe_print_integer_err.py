#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print(f"value = {value:d}")
        return True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
