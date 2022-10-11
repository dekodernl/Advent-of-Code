#!/usr/bin/python

def get_data():
    f = open('day01-puzzle-input.txt', "r")
    return f.readline().strip()

def solution():
    data = get_data()
    floor = 0
    position = 0
    while floor != -1:
        if data[position] == "(":
            floor += 1
        else:
            floor -= 1
        position += 1
        if floor == -1:
            return position

    return 0

if __name__ == "__main__":
    result = solution()
    print(result)
