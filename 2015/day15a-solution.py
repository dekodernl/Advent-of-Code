#!/usr/bin/python
from itertools import permutations as perms

def solution():
    ingredients = ["Sugar", "Sprinkles", "Candy", "Chocolate"]
    capacity = [3, -3, -1, 0]
    durability = [0, 3, 0, 0]
    flavor = [0, 0, 4, -2]
    texture = [-3, 0, 0, 2]
    calories = [2, 9, 1, 8]
    
    high_score = 0
    high_score_spoons = ()
    for spoons in list(perms(range(1, 101), len(ingredients))):
        if sum(spoons) == 100:
            score = 0
            c = sum([a * b for a, b in zip(spoons, capacity)])
            d = sum([a * b for a, b in zip(spoons, durability)])
            f = sum([a * b for a, b in zip(spoons, flavor)])
            t = sum([a * b for a, b in zip(spoons, texture)])

            if c >= 0 and d >= 0 and f >= 0 and t >= 0:
                score = c * d *  f * t
            if score > high_score:
                high_score = score
                high_score_spoons = spoons

    return (high_score, high_score_spoons) 

if __name__ == "__main__":
    result = solution()
    print(result)
