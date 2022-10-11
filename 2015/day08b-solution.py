#!/usr/bin/python
import re

def get_data():
    with open('day08-puzzle-input.txt') as f:
        lines = [r"{}".format(line.strip()) for line in f]
    return lines

def solution():
    data = get_data()

    lengths = []
    for i in data:
        codelen = len(i)
        chars = i[1:-1]
        chars = re.sub(r'\\', '\\\\\\\\', chars)
        chars = re.sub(r'\"', '\\\"', chars)
        chars = '"\\\"' + chars + '"\\\"'
        charlen = len(chars)
        lengths.append(charlen - codelen)

    return sum(lengths)

if __name__ == "__main__":
    result = solution()
    print(result)
