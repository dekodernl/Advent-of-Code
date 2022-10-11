#!/usr/bin/python

def get_data():
    f = open('day01-puzzle-input.txt', "r")
    return f.readline().strip()

def solution():
    data = get_data()
    return data.count("(") - data.count(")")

if __name__ == "__main__":
    result = solution()
    print(result)
