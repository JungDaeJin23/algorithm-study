T = int(input())
# (5 ≤ N ≤ 50)
# 직선 파이프는 90도 회전이 가능하며, 꺾인 파이프는 90, 180, 270도 회전이 가능하다.
#  최상단 좌측 파이프(시작 지점)는 반드시 왼쪽(in)과 연결되어야 하며,
#  최하단 우측 파이프(마지막 지점)은 반드시 오른쪽(out)과 연결되어야 한다.
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상하
next_idx = [[0, 1, 2, 3], ]


def backtracking(cnt=0, row=0, col=0):
    global ans, N, used, dr, dc
    if cnt >= ans:
        return
    if row == N-1 and col == N-1:
        if cnt < ans:
            ans = cnt
        return

    for d in next_idx:
        nr = row + dr[d]
        nc = col + dr[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or used[nr][nc] == 1:  # or matrix[nr][nc] == 0:
            continue
        # up
        if d == 0
            backtracking(cnt=cnt+1, row=nr, col=nc)
        # down
        elif d == 1:
            pass
        # left
        elif d == 2:
            pass
        # right
        else:
            pass


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    used[0][0] = 1
    ans = N*N
    backtracking()
    print('#{0} {1}'.format(tc, ans))
