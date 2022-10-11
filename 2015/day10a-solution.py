#!/usr/bin/python
# used generic look say logic from https://stackoverflow.com/a/6972836/690645
from itertools import groupby

def get_data():
    f = open('day10-puzzle-input.txt', "r")
    return f.readline().strip()

def solution():
    data = get_data()
    for i in range(40):
        data = ''.join( str(len(list(g))) + k for k, g in groupby(str(data)))
    
    return len(str(data))

if __name__ == "__main__":
    result = solution()
    print(result)
