#!/usr/bin/python3
with open ('./02.data') as f:
    lines = [line.rstrip() for line in f]

options = ["A", "B", "C"]

my_score = 0
for line in lines:
    u, i = line.split(" ")
    if i == "Z": # win
        my_score += 6
        my_score += options.index( options[(options.index(u) + 1) % 3] ) + 1
    elif i == "Y": # equ
        my_score += 3
        my_score += options.index(u) + 1
    else: #loss
        my_score += options.index( options[(options.index(u) - 1) % 3] ) + 1
     
print(my_score)
