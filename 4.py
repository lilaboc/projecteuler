result = []
for x in range(100, 999):
    for y in range(100, 999):
        z = x * y
        if str(z)[:] == str(z)[::-1]:
            result.append(z)
result.sort()
print(result[-1])
