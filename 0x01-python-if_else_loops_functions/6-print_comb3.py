#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if (j == i):
            continue
        if (i == 8 and j == 9):
            print(f"{i}{j}")
            continue
        if (j != 0 and i != 10):
            print(f"{i}{j}", end=", ")
