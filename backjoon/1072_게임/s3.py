X, Y = map(int, input().split())
# 100*Y / X = A(실수부) + B(소수부) >= A
# 100*(Y + k) / (X + k) = A+1 +B'(이식의 소수부) >= A+1
A = 100*Y//X
if A >= 99:
    cnt = -1
else:
    k = ((1+A) * X - 100 * Y) / (99-A)
    cnt = int(k)
    if k - cnt > 0:
        cnt += 1
print(cnt)