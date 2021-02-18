a = 1
b = 1
c = 2
while True:
    a, b = a + b, a
    c += 1
    if len(str(a)) == 1000:
        print(c)
        break