import string
with open('22.txt', 'r') as f:
    names = [name[1:-1] for name in f.read().split(',')]
    names.sort()
    r = 0
    for i in range(len(names)):
        r += sum(string.ascii_uppercase.index(o) + 1 for o in names[i]) * (i + 1)
    print(r)