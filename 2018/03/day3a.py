from collections import Counter
import itertools
import re

fn = "data.txt"
f = open(fn, "r")
data = f.read().split("\n")[:-1]

def parse_claim(claim_str):
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
claims = [parse_claim(c) for c in data]

# set fabricssize
fabricsize = [0, 0]
for (claim, left, top, width, height) in claims:
    fabricsize[0] = max(fabricsize[0], left + width)
    fabricsize[1] = max(fabricsize[1], top + height)

# create zeroed out grid
fabric = [[0] * (fabricsize[0] + 1) for i in range(fabricsize[1] + 1)]

# process all claims on to fabrics
for (claim, left, top, width, height) in claims:
    for x in range(left, left+width):
        for y in range(top, top + height):
            if fabric[x][y] is not 3:
                fabric[x][y] += 1
            if fabric[x][y] == 2:
                fabric[x][y] = 3

# count all occurences of each value in the fabric
counts = Counter(list(itertools.chain.from_iterable(fabric)))
print(counts[3])
