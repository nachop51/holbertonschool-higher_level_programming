#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirs = dir(hidden_4)
    for directory in dirs:
        if "__" not in directory:
            print(directory)
