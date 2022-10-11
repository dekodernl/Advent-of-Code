#!/usr/bin/python
from math import ceil, floor
from load_puzzle_data import load_list
seats = [[0 for y in range(8)] for x in range(128)]
lines = load_list(5)
for line in lines:
    low, high = 0, 127
    for i in range(0, 6):
        if line[i] == 'F':
            high = floor((low + high) / 2)
        elif line[i] == 'B':
            low = ceil((low + high) / 2)
    if line[6] == 'F':
        row = low
    else:
        row = high

    left, right = 0, 7
    for i in range(7, 10):
        if line[i] == 'R':
            left = floor((left + right) / 2)
        elif line[i] == 'L':
            right = ceil((left + right) / 2)
    if line[9] == 'L':
        col = left
    else:
        col = right
    
    seats[row][col] = 1

for y in range(0,128):
    s = ""
    _s = ""
    for x in range(0,8):
        _s += " " + str((y * 8) + x)
        s += " "+str(seats[y][x])

    print(s, _s)
