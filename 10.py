n = 2000000
# n = 10
a = [True] * n

for i in range(2, n):
    for o in range(i * 2, n, i):
        a[o] = False

print(a)
print(sum(i for i in range(2, n) if a[i]))

