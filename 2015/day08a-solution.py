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
        chars = re.sub(r'\\x[0-9a-f][0-9a-f]', 'X', chars)
        chars = re.sub(r'\\\"', 'Z', chars)
        chars = re.sub(r'\\\\', 'Y', chars)
        charlen = len(chars)
        lengths.append(codelen - charlen)

    return sum(lengths)

if __name__ == "__main__":
    result = solution()
    print(result)
