l = 1
s = 1
for i in range(1, 501):
    step = 2 * i
    s += l * 4 + step * 10
    l += step * 4
    print(s)
    