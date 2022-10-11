f = open("data.txt", "r")
data = f.read().split("\n")
total = sum([int(value) for value in data[:-1]])
print(total)

