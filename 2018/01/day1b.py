f = open("data.txt", "r")
data = f.read().split("\n")[:-1]
total = 0
totals = []
cursor = 0
len_data = len(data)
while len(set(totals)) == len(totals):
    total = total + int(data[cursor])

    print(total)
    totals.append(total)
    cursor += 1
    if cursor == len_data:
        cursor = 0
    
