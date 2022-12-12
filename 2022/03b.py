#!/usr/bin/python3
with open ('./03.data') as f:
    rucksacks = [line.rstrip() for line in f]

priority_sum = 0
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    items = sorted(list(set([j for i in group for j in i])))
    
    for item in items:
        if item in group[0] and item in group[1] and item in group[2]:
            priority_sum += chars.index(item) + 1

print(priority_sum)

    


