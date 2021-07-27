N = int(input())
# x, y, d, g
#  x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dragon_curve_info = [list(map(int, input().split())) for _ in range(N)]
#  격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.
board = [[0]*101 for _ in range(101)]
for x, y, d, g in dragon_curve_info:
    position_stack = []
    board[y][x] = 1
    position_stack.append((y, x))
    nr = y + dr[d]
    nc = x + dc[d]
    board[nr][nc] = 1
    position_stack.append((nr, nc))
    for _ in range(g):
        repeatation = len(position_stack) - 1
        turing_point = position_stack[-1]
        for idx in range(repeatation-1, -1, -1):
            delta_r = position_stack[idx][0] - turing_point[0]
            delta_c = position_stack[idx][1] - turing_point[1]
            delta_r *= -1
            nr = turing_point[0] + delta_c
            nc = turing_point[1] + delta_r
            board[nr][nc] = 1
            position_stack.append((nr, nc))

cnt = 0
for row in range(100):
    for col in range(100):
        if board[row][col] and board[row][col+1] and board[row+1][col] and board[row+1][col+1]:
            # print(row, col)
            cnt += 1
print(cnt)