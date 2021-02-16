


cache = {}
m = 0


def collatz(n):
    c = 1
    t = n 
    while True:
        if t == 1:
            break
        if t % 2 == 0:
            t = int(t / 2)
        else:
            t = t * 3 + 1
        if t in cache:
            return c + cache[t]
        c += 1
    cache[n] = c
    return c



m = 0
s = 0
for i in range(1000000, 1, -1):
    r = collatz(i)
    if r > m:
        m = r
        s = i
print(s)