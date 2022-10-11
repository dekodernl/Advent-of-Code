#!/usr/bin/python
from itertools import permutations, combinations

def get_data():
    data = {}
    f = open('day13-puzzle-input.txt', "r")
    lines = f.readlines()

    for line in lines:
        line = line.strip().replace(' would lose ',' -')\
            .replace(' would gain ', ' ')\
            .replace(' happiness units by sitting next to ', ' ')\
            .replace('.', '')
        line = line.split(' ')
        line[1] = int(line[1])
    
        if line[0] not in data.keys():
            data[line[0]] = {}
        data[line[0]][line[2]] = line[1]
        data[line[0]]['Bas'] = 0

    data['Bas'] = {}
    for key in data.keys():
        data['Bas'][key] = 0
    return data
    
def solution():

    data = get_data()

    attendees = list(data.keys())
    highest = (2 ** 16) * -1
    al = len(attendees)
    for seating in permutations(range(0, al), al):
        happiness = []
        for chair in seating:
            left = attendees[seating[(chair - 1) % al]]
            me = attendees[seating[chair]]
            right = attendees[seating[(chair + 1) % al]]

            happiness.append(data[me][left])
            happiness.append(data[me][right])

        total = sum(happiness)

        if total > highest:
            highest = total
            highest_happiness = happiness
            highest_seating = [attendees[chair] for chair in seating]

    return highest

if __name__ == "__main__":
    result = solution()
    print(result)
