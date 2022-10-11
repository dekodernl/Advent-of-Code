#!/usr/bin/python
import json

def get_data():
    f = open('day12-puzzle-input.txt', "r")
    return f.readlines()

def node(obj):

    subtotal = 0
  
    if isinstance(obj, dict):
        if "red" not in obj.values():
            for key in obj:
                subtotal += node(obj[key])

    elif isinstance(obj, list):
        for val in obj:
            if val != "red":
                subtotal += node(val)

    elif isinstance(obj, int):
        return obj

    return subtotal

def solution():
    data = get_data()
    doc = json.loads(data[1].strip())
    
    total = node(doc)
    return total

if __name__ == "__main__":
    result = solution()
    print(result)
