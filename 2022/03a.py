#!/usr/bin/python3
with open ('./03.data') as f:
    rucksacks = [line.rstrip() for line in f]

priority_sum = 0
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
for sack in rucksacks:
    ls = int(len(sack)/2)
    f = sack[0:ls]
    s  = sack[ls:]
    
    checked = []
    for c in f:
        if c not in checked and c in s:
            priority_sum += chars.index(c) + 1
            checked.append(c)

print(priority_sum)

    


