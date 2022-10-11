f = open("data.txt", "r")
data = f.read().split("\n")[:-1]
import collections
a, b = 0, 0
for box in data:
    box = list(set([v for k,v in collections.Counter(box).items() if v in [2,3]]))
    if 2 in box:
        a += 1
    if 3 in box:
        b += 1

print(a, b, a * b)
