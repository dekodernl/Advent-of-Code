#!/usr/bin/python3
import re
sop = 0
with open ('./06.data') as f:
    buffer = [line.rstrip() for line in f][0]
    cursor = 0
    searching = True
    while searching:
        subset = buffer[cursor:cursor+14]
        counts = 0
        for char in subset:
            counts += subset.count(char)
        if counts == 14:
            sop = cursor + subset.index(char) + 1
            searching = False
        cursor +=1
print(sop)
