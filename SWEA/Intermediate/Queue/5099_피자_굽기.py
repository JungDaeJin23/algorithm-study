from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    fire_pit = deque([(0, 0)] * N)
    done = [False] * (M + 1)
    cnt = 0
    idx = 0
    while cnt < M - 1:
        cheese = fire_pit[0][1]//2
        if cheese > 0:
            fire_pit[0] = (fire_pit[0][0], cheese)
        else:
            if fire_pit[0][0] > 0:
                cnt += 1
                done[fire_pit[0][0]] = True
            if idx < M:
                fire_pit[0] = (idx+1, ci[idx])
                idx += 1
            else:
                fire_pit[0] = (0, 0)
        fire_pit.rotate(1)
    ans = 0
    for idx in range(1, len(done)):
        if not done[idx]:
            ans = idx
            break
    print('#{0} {1}'.format(tc, ans))