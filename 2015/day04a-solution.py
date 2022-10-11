#!/usr/bin/python
import hashlib

def get_data():
    f = open('day04-puzzle-input.txt', "r")
    return f.readline().strip()

def solution():
    data = get_data()
    number = 1
    while True:
        md5 = hashlib.md5( ( data + str(number) ).encode() ).hexdigest()
        print(str(number) + (" " * 20), end="\r")
        if md5[:5] == "00000":
            return number
        number += 1

if __name__ == "__main__":
    result = solution()
    print(result)
