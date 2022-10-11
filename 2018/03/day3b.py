""" Advent of Code 2018 - day 3 part 2 """
import re

FN = "data.txt"
FP = open(FN, "r")
DATA = FP.read().split("\n")[:-1]

def parse_claim(claim_str):
    """ parse claim string to usable data """

    # use regex to extract data
    search = re.search(r'\#(\d+)\s\@\s(\d+)\,(\d+)\:\s(\d+)x(\d+)', claim_str)

    # return tuple of data (claim / left / top / width / height)
    return (
        int(search.group(1)),
        int(search.group(2)),
        int(search.group(3)),
        int(search.group(4)),
        int(search.group(5))
    )

# parse all claims
CLAIMS = [parse_claim(c) for c in DATA]

# set fabricssize
FABRICSIZE = [0, 0]
for (claim, left, top, width, height) in CLAIMS:
    FABRICSIZE[0] = max(FABRICSIZE[0], left + width)
    FABRICSIZE[1] = max(FABRICSIZE[1], top + height)

# create zeroed out grid
FABRIC = [[0] * (FABRICSIZE[0] + 1) for i in range(FABRICSIZE[1] + 1)]

# process all claims on to fabrics
for (claim, left, top, width, height) in CLAIMS:
    for x in range(left, left+width):
        for y in range(top, top + height):
            if FABRIC[x][y] is not 3:
                FABRIC[x][y] += 1
            if FABRIC[x][y] == 2:
                FABRIC[x][y] = 3

CLAIM_INTACT = True
# find where claim has not been damaged by other claim
for (claim, left, top, width, height) in CLAIMS:
    for x in range(left, left+width):
        for y in range(top, top + height):
            if FABRIC[x][y] != 1:
                CLAIM_INTACT = False

    if CLAIM_INTACT:
        print(claim)

    CLAIM_INTACT = True
