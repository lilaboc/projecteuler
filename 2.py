c = 2
a, b = 1, 2
while a < 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        c += b
print(c)

