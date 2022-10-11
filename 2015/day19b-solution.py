import re
from random import sample

replacements = {}
with open('puzzle-input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[:-2]:
        line = line.strip().split(' => ')
        replacements[line[1]]= line[0]
    inp = lines[-1].strip()

#pattern = re.compile('|'.join(replacements))

#https://github.com/adamb70/AdventOfCode2015/blob/master/19/19b.py
steps = 0
final = inp
while final != 'e':
    temp = final
    for n in sample(list(replacements), len(replacements)):
        if n in final:
            steps += final.count(n)
            final = final.replace(n, replacements[n])

    if final == temp:
        final = inp
        steps = 0
        continue

print(steps)
