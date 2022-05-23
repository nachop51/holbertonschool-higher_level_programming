#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("?", "?\n\n").replace(
        ".", ".\n\n").replace(":", ":\n\n")
    text = text.split("\n")
    for line in text:
        line = line.strip()
        print(line + "\n", end="")
