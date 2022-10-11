#!/usr/bin/python
import re
from itertools import permutations

def get_data():
    with open('day09-puzzle-input.txt') as f:
        lines = [r"{}".format(line.strip()) for line in f]
    return lines

def solution():
   
    data = get_data()
    locations = list(set(re.findall(r'([A-Z]\w+)', " ".join(data))))

    pairs = []
    for i in data:
        dist = re.findall(r'([A-Z]\w+)(?:\sto\s)([A-Z]\w+)(?:\s=\s)(\d{1,})' ,i)[0]
        pairs.append(dict(src=dist[0], dest=dist[1], dist=int(dist[2])))
        pairs.append(dict(src=dist[1], dest=dist[0], dist=int(dist[2])))

    highest = 0
    for c in permutations(range(len(locations)), len(locations)):
        dist = 0
        for i in range(0, len(c)-1):
            dist += [p['dist'] for p in pairs \
                     if p['src'] == locations[c[i]] \
                     and p['dest'] == locations[c[i+1]]][0]
        if dist > highest:
            highest = dist

    return highest

if __name__ == "__main__":
    result = solution()
    print(result)
