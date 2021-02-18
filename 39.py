r = 0
m = 0
for p in range(3, 1001):
    s = 0
    print(p)
    for a in range(1, p - 2):
        for b in range(1, p - 1):
            c = p - a - b
            if c * c == a * a + b * b:
                s += 1

    if s > m:
        m = s
        r = p
print(r)