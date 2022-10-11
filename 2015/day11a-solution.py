#!/usr/bin/python
import re

def get_data():
    f = open('day11-puzzle-input.txt', "r")
    return f.readline().strip()

chars = 'abcdefdghijklmnopqrstuvwxyz'
threes = [chars[n:n+3] for n in range(0, len(chars)-2)]

def increment(pwd):
    if pwd[-1] == 'z':
        return increment(pwd[:-1]) + "a"
    next_char = chr(ord(pwd[-1])+1)
    if next_char in 'oil':
        next_char = chr(ord(next_char)+1)
    return pwd[:-1] + next_char

def check_pass(pwd):
    c = re.findall(r'(i|o|l)', pwd)
    if len(c) > 0:
        return False
    c = list(set(re.findall(r'(\w)\1{1,}', pwd)))
    if len(c) == 2 and c[0] != c[1]:
        for ts in threes:
            if ts in pwd:
                return True
    return False

def solution():

    password = get_data()

    while True:
        password = increment(password)
        if check_pass(password):
            return password
    return None

if __name__ == "__main__":
    result = solution()
    print(result)
