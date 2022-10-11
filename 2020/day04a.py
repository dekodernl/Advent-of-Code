#!/usr/bin/python
import re
from load_puzzle_data import load_list

lines = load_list(4)

passports = []

data = []
item = {}
for line in lines:
    if line == "":
        data.append(item)
        item = {}
    line = line.split(" ")
    if line[0] != "":
        for l in line:
            prop = l.split(":")
            item[prop[0]] = prop[1]
properties = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for item in data:
    s = sum([1 for prop in properties if prop in item.keys()])
    if s == len(properties):
        valid += 1
print(valid)

