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
valid_passports = 0
for item in data:
    valid = []
    s = sum([1 for prop in properties if prop in item.keys()])

    if s == len(properties):
        # birth year
        if int(item['byr']) in range(1920, 2003):
            valid.append(1)
        
        # issue year
        if int(item['iyr']) in range(2010, 2021):
            valid.append(1) 
        
        # expiration year
        if int(item['eyr']) in range(2020, 2031):
            valid.append(1) 
        
        # height
        hgt = re.findall(r'(\d{2,3})(cm|in){0,1}', item['hgt'])[0]
        if hgt[1] == 'cm' and int(hgt[0]) in range(150, 194):
            valid.append(1)
        elif hgt[1] == 'in' and int(hgt[0]) in range(59, 77):
            valid.append(1)

        # hair color
        if len(re.findall(r'\#[a-f0-9]{6}', item['hcl'])) == 1:
            valid.append(1)
        
        # eye color
        if item['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            valid.append(1)

        # passport id
        if len(re.findall(r'^[0-9]{9}$', item['pid'])) == 1:
            valid.append(1)
        
        # if all 7 conditions are met
        if sum(valid) == 7:
            valid_passports += 1

print(valid_passports)

