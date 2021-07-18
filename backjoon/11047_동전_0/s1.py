N, change = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
idx = N - 1
while change:
    cnt += change // coins[idx]
    change %= coins[idx]
    idx -= 1
print(cnt)