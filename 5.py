s = 1
while True:
    for i in range(1, 21):
        if s % i != 0:
            break
    else:
        print(s)
        break
    s += 1