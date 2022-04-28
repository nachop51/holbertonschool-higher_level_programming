#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        s = "arguments."
    elif len(sys.argv) - 1 == 1:
        s = "argument:"
    else:
        s = "arguments:"
    print(len(sys.argv) - 1, s)
    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"{i}: {v}")
