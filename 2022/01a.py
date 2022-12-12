#!/usr/bin/python3
elves = []
elf = []
with open ('./01.data') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    if line == "":
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line))

highest = 0
for e in elves:
    se =  sum(e)
    if se > highest:
        highest = se

print(highest)
