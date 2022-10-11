import json

def solution():

    with open('puzzle-input.txt') as json_file:
        aunts = json.load(json_file)
    
    dna = {
        "children": range(3,4),
        "cats": range(7,100),
        "samoyeds": range(2,3),
        "pomeranians": range(0,4),
        "akitas": range(0,1),
        "vizslas": range(0,1),
        "goldfish": range(0,6),
        "trees": range(3,100),
        "cars": range(2,3),
        "perfumes": range(1,2),
    }
   
    for i, aunt in enumerate(aunts):
        matches = 0
        for prop in aunt.keys():
            if aunt[prop] in dna[prop]:
                matches += 1
        if matches == 3:
            print(i + 1, aunt)
if __name__ == "__main__":
    result = solution()
