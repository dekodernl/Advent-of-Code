#!/usr/bin/python

def get_data():
    f = open('day03-puzzle-input.txt', "r")
    return f.readline()

def solution():
    data = get_data()
    x, y = 0, 0
    
    houses = dict({ (0,0) : 1 })

    data = str(data)\
        .replace("^", "N")\
        .replace(">", "E")\
        .replace("v", "S")\
        .replace("<", "W")

    for move in data:
        
        if move == 'N':
            y += 1
        elif move == 'E':
            x += 1
        elif move == 'S':
            y -= 1
        elif move == 'W':
            x -= 1
        
        if (x,y) in houses.keys():
            houses[(x,y)] += 1
        else:
            houses[(x,y)] = 1

    return len(houses)

if __name__ == "__main__":
    result = solution()
    print(result)
