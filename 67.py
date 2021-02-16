r = []
with open('67.txt', 'r') as f:
    for line in f.readlines():
        r.append([int(i) for i in line.split()])


print(r)
for row_number in range(1, len(r)):
    for item_number in range(len(r[row_number])):
        if item_number == 0:
            r[row_number][item_number] += r[row_number - 1][item_number]
        elif item_number == len(r[row_number]) - 1:
            r[row_number][item_number] += r[row_number - 1][item_number - 1]
        else:
            r[row_number][item_number] += max(r[row_number - 1][item_number - 1], r[row_number - 1][item_number])
print(r)
print(max(r[-1]))




