for a in range(1, 998):
    for b in range(a, 998):
        for c in range(b, 998):
            if a + b + c == 1000 and pow(a, 2) + pow(b, 2) == pow(c, 2):
                print(a * b * c)
                break