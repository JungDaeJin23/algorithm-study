# reverse thinking; think in reverse
# start process from b until a


A, B = map(int, input().split())
cnt = 0

while A < B:
    cnt += 1
    if B % 10 == 1:
        B //= 10
    elif B%2 == 0:
        B //= 2
    else:
        break
print(cnt + 1 if A == B else -1)

