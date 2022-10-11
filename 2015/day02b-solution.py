#!/usr/bin/python

def get_data():
    f = open('day02-puzzle-input.txt', "r")
    lines = f.readlines()
    return [ [ int(l), int(w), int(h) ] for l, w, h in [ lin.replace("\n", "").split("x") for lin in lines] ]

def solution():
    data = get_data()
    total_feet_of_ribbon = 0
    for (l, w, h) in data:
        total_feet_of_ribbon += (2 * l) + (2 * w) + (2 * h) - (2 * max(l, w, h)) + (l * w * h)
    return total_feet_of_ribbon

if __name__ == "__main__":
    result = solution()
    print(result)
