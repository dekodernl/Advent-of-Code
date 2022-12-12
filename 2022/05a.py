#!/usr/bin/python3
import re

p_crate = re.compile(r'.(.).\s?')
p_moves = re.compile(r'\d+')
with open ('./05.data') as f:
    lines = [line.rstrip() for line in f]
    stacks = [ [''] * 8 for i in range(9)]

    # create stacks
    for i in range(0,8):
        for cid, crate in enumerate(re.findall(p_crate, lines[i])):
            stacks[cid][7-i] = crate

    for idx, stack in enumerate(stacks):
        stack[:] = [x for x in stack if x not in ["", " "]]
        stacks[idx] = stack
    
    # move stuff arround
    moves = []
    for i in range(10, len(lines)):
        q, f, t  = re.findall(p_moves, lines[i])
        for i in range(0, int(q)):
            crate = stacks[int(f)-1].pop()
            stacks[int(t)-1].append(crate)

code = ""
for s in stacks:
    code += s[len(s)-1]

print(code)
