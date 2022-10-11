import json

def solution():

    with open('puzzle-input.txt') as json_file:
        aunts = json.load(json_file)
    
    dna = {
	"children:": 3,
	"cats:": 7,
	"samoyeds:": 2,
	"pomeranians:": 3,
	"akitas:": 0,
	"vizslas:": 0,
	"goldfish:": 5,
	"trees:": 3,
	"cars:": 2,
	"perfumes:": 1
    }
   
    for i, aunt in enumerate(aunts):
        props = list(aunt.keys())
        if dna[props[0]] == aunt[props[0]]\
                and dna[props[1]] == aunt[props[1]]\
                and dna[props[2]] == aunt[props[2]]:
            print(i + 1, aunt)
         
            



if __name__ == "__main__":
    result = solution()
    print(result)
