#!/usr/bin/python

def get_data():
    f = open('day02-puzzle-input.txt', "r")
    lines = f.readlines()
    return [ [ int(l), int(w), int(h) ] for l, w, h in [ lin.replace("\n", "").split("x") for lin in lines] ]

def solution():
    data = get_data()
    total_wrapping_paper = 0
    for (l, w, h) in data:
        surfaces = [2*l*w, 2*w*h, 2*h*l]
        total_wrapping_paper += sum(surfaces) + min(l*w,w*h,h*l)
    return total_wrapping_paper

if __name__ == "__main__":
    result = solution()
    print(result)
