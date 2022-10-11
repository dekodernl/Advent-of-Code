#!/usr/bin/python
import re

def read_file(day, strip=True, string=False):
    with open('day{:02d}-puzzle-input.txt'.format(int(day)), 'r') as f:
        if strip:
            if string:
                return "".join([line.strip() for line in f.readlines()])
            return [line.strip() for line in f.readlines()] 
        if string:
            return "".join([line for line in f.readlines()])
        return [line for line in f.readlines()] 

def load_list(day, integers=False):
    data = read_file(day)
    if integers:
        return [int(val) for val in data]
    return data

