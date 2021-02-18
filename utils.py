def sieve(n):
    a = [True] * n
    a[0] = False
    for i in range(2, n):
        if i % 1000000 == 0:
            print(i)
        if not a[i]:
            continue
        for o in range(i * 2, n, i):
            if a[o]:
                a[o] = False
    return a