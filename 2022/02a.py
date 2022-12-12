#!/usr/bin/python3
with open ('./02.data') as f:
    lines = [line.rstrip() for line in f]

left = "A,B,C".split(",")
right = "X,Y,Z".split(",")

wins = ["A Y","B Z","C X"]
equs = ["A X","B Y", "C Z"]

my_score = 0
for line in lines:
    l, r = line.split(" ")
    u = left.index(l) + 1
    i = right.index(r) + 1
    
    my_score += i
    
    if line in wins:
        my_score += 6
    elif line in equs:
        my_score += 3

print(my_score) 
