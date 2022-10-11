#!/usr/bin/python
from load_puzzle_data import read_file
groups = read_file(6, False, True).split("\n\n")

yes = 0
for group in groups:
    yes += len(list(set(list(group.replace('\n','')))))

print(yes)
