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

highest = []
for e in elves:
    se =  sum(e)
    highest.append(se)

sh = sorted(highest)
print(sum(sh[-3:]))
