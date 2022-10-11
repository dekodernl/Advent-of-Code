#!/usr/bin/python
import re

def get_data():
    f = open('day12-puzzle-input.txt', "r")
    return f.readlines()

def solution():
    pi = get_data()
    return sum([int(i) for i in re.findall(r'\-?\d{1,}', str(pi))])

if __name__ == "__main__":
    result = solution()
    print(result)
