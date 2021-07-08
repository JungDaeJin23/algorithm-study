X, Y = map(int, input().split())
A = 100*Y//X
if A >= 99:
    cnt = -1
else:
    cnt = X // (99-A)
    if X % (99-A):
        cnt += 1
print(cnt)