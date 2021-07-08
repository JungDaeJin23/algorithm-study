X, Y = map(int, input().split())
A = 100*Y//X
if A >= 99:
    cnt = -1
else:
    k = ((1+A) * X - 100 * Y) / (99-A)
    cnt = int(k)
    if k - cnt > 0:
        cnt += 1
print(cnt)