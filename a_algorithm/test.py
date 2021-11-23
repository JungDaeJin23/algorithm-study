from itertools import combinations
a = combinations([1,2,3,4,5,6], 3)
for d, b, c in a:
    print(d, b, c)