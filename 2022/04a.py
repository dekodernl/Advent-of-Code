#!/usr/bin/python3
import re
with open ('./04.data') as f:
    assignments = [line.rstrip() for line in f]

p = re.compile(r'\d+')
pairs = 0
for assignment in assignments:
    n = [int(x) for x in p.findall(assignment)]
    a = range(n[0], n[1]+1)
    b = range(n[2], n[3]+1)
    c = list(set(a) & set(b))

    if len(a) == len(c) or len(b) == len(c):
        pairs += 1

print(pairs)


