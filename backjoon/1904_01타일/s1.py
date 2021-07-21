N = int(input())
a = 1
b = 2
if N <= 2:
    print(N)
else:
    for _ in range(N-2):
        a, b = b, a + b
        # print(b, b%15746)
    print(b%15746)