from copy import deepcopy
from beepy import beep
from colored import fg, bg, attr

def get_data():
    with open("puzzle-input.txt") as f:
        data = f.readline()
    return data.strip().replace('#','1').replace('.','0')

def printer(grid, size, colors=[]):

    for y in range(0, size):
        for x in range(0, size):
            if grid[y][x] == 1:
                print('%s%s%s%s' % (fg(2), attr(1), '▇', attr(0)), end=" ")
            else:
                print(grid[y][x], end=" ")

        print("\r")

    print()

def solution():

    size = 100
    grid = [[ 0 for j in range(size)] for i in range(size) ]
    gridsize = size * size

    data = get_data()

    for i, p in enumerate(data):
        dm = divmod(i, size)
        grid[dm[0]][dm[1]] = int(p)

    for toggle in range(0, 100):
        new_grid = deepcopy(grid)
        for y in range(size):
            for x in range(size):
                neighbour_xy = [
                    (x,y+1),
                    (x+1,y+1),
                    (x+1,y),
                    (x+1,y-1),
                    (x,y-1),
                    (x-1,y-1),
                    (x-1,y),
                    (x-1,y+1)
                ]
                
                neighbours = []
                ns =[]
                for _x,_y in neighbour_xy:
                    ns.append((_x, _y))
                    if _x in range(size) and _y in range(size):
                        neighbours.append(grid[_y][_x])
                    else:
                        neighbours.append(9)
                lights_on = neighbours.count(1)
                if grid[y][x] == 1:
                    if lights_on != 2 and lights_on != 3:
                        new_grid[y][x] = 0
                        
                elif grid[y][x] == 0:
                    if lights_on == 3:
                        new_grid[y][x] = 1
        grid = deepcopy(new_grid)

    printer(grid, size)
    print(sum([row.count(1) for row in grid]))

    beep(sound=5)

solution()
