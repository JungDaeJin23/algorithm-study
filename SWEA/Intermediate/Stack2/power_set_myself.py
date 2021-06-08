a = [1, 2, 3, 4]
d = [0]*len(a)


def backtrack(a, k, n):
    global d
    if k == n:
        for i in range(len(a)):
            if d[i]:
                print(a[i], end=' ')
        print(',')
    else:
        for j in range(1, -1, -1):
            # 1 먼저 해야 [1, 1, 1, 1] true
            d[k] = j
            backtrack(a, k+1, n)


backtrack(a, 0, len(a))
