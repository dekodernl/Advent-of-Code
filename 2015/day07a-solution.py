#!/usr/bin/python
import re

def get_data():
    f = open('day07-puzzle-input.txt', "r")
    return f.readlines()

def solution():
    data = get_data()
    cmds = []
    for instruction in data:
        inst = instruction.strip().split(" -> ")
        output = inst.pop()
        cmd = (re.findall(r"(NOT|AND|OR|RSHIFT|LSHIFT)", inst[0]) or ["SET"]).pop()
        values = inst[0].replace(cmd + " ", "").split(" ")
        cmds.append((cmd, values, output)) 

    strints = [str(i) for i in range(0, 2**16)]

    wires = {}
    index = 0
    while len(cmds) > 0:
        cmd, values, output = cmds[index]
        set_values = []
        for val in values:
            if val in strints:
                set_values.append(int(val))
            elif val in wires.keys() and int(wires[val]) >= 0:
                set_values.append(wires[val])
        
        if len(values) == len(set_values):
            if cmd == 'AND':
                wires[output] = set_values[0] & set_values[1]
            elif cmd == 'OR':
                wires[output] = set_values[0] | set_values[1]
            elif cmd == 'LSHIFT':
                wires[output] = set_values[0] << set_values[1]
            elif cmd == 'RSHIFT':
                wires[output] = set_values[0] >> set_values[1]
            elif cmd == 'NOT':
                wires[output] = (1 << 16) - 1 - set_values[0]
            elif cmd == 'SET':
                wires[output] = set_values[0]

            del cmds[index]
            index = 0
        else:
            index += 1

    return wires['a']

if __name__ == "__main__":
    result = solution()
    print(result)
