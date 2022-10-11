#!/usr/bin/python
from functools import reduce
from load_puzzle_data import load_list

lines = load_list(3)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

tree_counts = []
for right, down in slopes:
    x = 0
    y = 0
    tree_count = 0
    for line_no in range(0, len(lines), down ):
        if lines[line_no][x % len(lines[line_no])] == "#":
            tree_count +=1
        x += right
    tree_counts.append(tree_count)
print(reduce(lambda x, y: x*y, tree_counts))
