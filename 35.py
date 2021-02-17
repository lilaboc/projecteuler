def circular(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:] + s[:i])




n = 1000000
# n = 10
a = [True] * n

for i in range(2, n):
    for o in range(i * 2, n, i):
        a[o] = False

r = 0
for i in range(2, n):
    if all(a[o] for o in circular(i)):
        r += 1
print(r)



# print(sum(i for i in range(2, n) if a[i]))
