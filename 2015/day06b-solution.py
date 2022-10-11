#!/usr/bin/python
import re

def get_data():
    f = open('day06-puzzle-input.txt', "r")
    data = f.readlines()
    instructions = []
    for line in data:
        pattern = r"(toggle|turn off|turn on)(?:\s)"\
            "(\d{1,3})\,(\d{1,3})(?:\sthrough\s)(\d{1,3})\,(\d{1,3})"
        m = re.findall(pattern, line)
        instructions.append((m[0][0], [int(i) for i in m[0][1:]]))
    return instructions

def solution():
    instructions = get_data()
    size = 1000
    grid = [[0 for x in range(size)] for x in range(size)]

    for action, coordinates in instructions:
        ax, ay, bx, by = coordinates
        for y in range(ay, by+1):
            for x in range(ax, bx+1):
                if action == 'toggle':
                    grid[y][x] += 2
                elif action == 'turn on':
                    grid[y][x] += 1
                else:
                    grid[y][x] -= 1

                if grid[y][x] < 0:
                    grid[y][x] = 0

    lights_shining = sum(grid, [])

    return sum(lights_shining)

if __name__ == "__main__":
    result = solution()
    print(result)
