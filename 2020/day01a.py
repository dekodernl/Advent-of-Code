#!/usr/bin/python
from load_puzzle_data import load_list

data = load_list(1, True)

options = []
for i in data:
    remainder = 2020 - i
    if remainder in data:
        print(remainder * i)
        break
        
