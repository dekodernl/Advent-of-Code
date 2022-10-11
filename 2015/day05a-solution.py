#!/usr/bin/python

def get_data():
    f = open('day05-puzzle-input.txt', "r")
    return f.readlines()

def naughty_or_nice(string):
    # rule 1 - contains three vowels
    vowels = []
    enough_vowels = False
    for char in string:
        if char in 'aeoiu':
            vowels.append(char)
    if len(vowels) > 2:
        enough_vowels = True

    # rule 2 - contains two consecutive values
    consecutive_found = False
    pos = 0
    while pos < len(string) - 1:
        if string[pos] == string[pos+1]:
            consecutive_found = True
            break
        pos += 1

    # rule 3 - does not contain ab, cd, pq or xy
    contains_no_stuff = True
    for ignore in ['ab', 'cd', 'pq', 'xy']:
        if ignore in string:
            contains_no_stuff = False
            break

    if contains_no_stuff and enough_vowels and consecutive_found:
        return True
    return False


def solution():
    data = get_data()

    nice_strings = []
    naugthy_strings = []

    for string in data:
        if naughty_or_nice(string):
            nice_strings.append(string)
        else:
            naugthy_strings.append(string)

    return len(nice_strings)

if __name__ == "__main__":
    result = solution()
    print(result)
