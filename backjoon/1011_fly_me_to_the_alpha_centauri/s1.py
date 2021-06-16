T = int(input())

for tc in range(T):
    x, y = map(int, input().split())
    cnt = 0
    distance = 0
    target = y-x
    while distance < target:
        distance += cnt//2 + 1
        cnt += 1
    print(cnt)
