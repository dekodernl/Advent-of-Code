#!/usr/bin/python
from load_puzzle_data import load_list

data = load_list(1, True)

for idx, expense in enumerate(data):
    for i in range(idx, len(data)):
        remainder = 2020 - expense - data[i]
        if remainder in data:
            print(expense * data[i] * remainder)
            exit()
