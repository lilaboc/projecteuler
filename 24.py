from itertools import permutations  


for i, v in enumerate(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
    if i == 1000000 - 1:
        print(v)
        break


