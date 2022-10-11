f = open("data.txt", "r")
data = f.read().split("\n")[:-1]

for a in data:
    for b in data:
        if a != b:
            for i in range(0, len(b)):
                _a = list(a)
                _b = list(b)
                del _a[i]
                del _b[i]
                if "".join(_a) == "".join(_b):
                    print("".join(_a), "".join(_b))
