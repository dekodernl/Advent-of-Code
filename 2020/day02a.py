#!/usr/bin/python
from load_puzzle_data import load_list
import re

data = load_list(2)
regex = r'(\d{1,2})\-(\d{1,2})\s([a-z])\:\s([a-z]{1,})'

count = 0
for line in data:
    low, high, letter, password = re.findall(regex, line).pop()
    if password.count(letter) in range(int(low), int(high) + 1):
        count += 1
print(count)
