N = int(input())
desert = [list(map(int, input().split())) for _ in range(N)]
r = c = N // 2
direction = 0
# left, down, right, up
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
# percent
answer = 0
dist = 1
cnt = 0
flag = 0
# percent_board = [[0, 0, 0.02, 0, 0],
#                  [0, 0.1, 0.07, 0.01, 0],
#                  [0.05, 0, 0, 0, 0],
#                  [0, 0.1, 0.07, 0.01, 0],
#                  [0, 0, 0.02, 0, 0]]
for _ in range(1, N**2):
    r += dr[direction]
    c += dc[direction]

    total = 0
    # 7 percent
    tmp = int(desert[r][c] * 0.07)
    nr = r + dc[direction]
    nc = c + dr[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp
    nr = r - dc[direction]
    nc = c - dr[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp
    # 10 percent
    tmp = int(desert[r][c] * 0.1)
    nr = r + dc[direction] + dr[direction]
    nc = c + dr[direction] + dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp
    nr = r - dc[direction] + dr[direction]
    nc = c - dr[direction] + dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp

    # 1 percent
    tmp = int(desert[r][c] * 0.01)
    nr = r + dc[direction] - dr[direction]
    nc = c + dr[direction] - dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp

    nr = r - dc[direction] - dr[direction]
    nc = c - dr[direction] - dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp

    # 2 percent
    tmp = int(desert[r][c] * 0.02)
    nr = r + 2 * dc[direction]
    nc = c + 2 * dr[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp
    nr = r - 2 * dc[direction]
    nc = c - 2 * dr[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp

    # 5 percent
    tmp = int(desert[r][c] * 0.05)
    nr = r + 2 * dr[direction]
    nc = c + 2 * dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += tmp
    else:
        answer += tmp
    total += tmp

    # alpha
    desert[r][c] -= total
    nr = r + dr[direction]
    nc = c + dc[direction]
    if 0 <= nr < N and 0 <= nc < N:
        desert[nr][nc] += desert[r][c]
    else:
        answer += desert[r][c]
    desert[r][c] = 0

    cnt += 1
    if cnt == dist:
        flag += 1
        cnt = 0
        if flag == 2:
            flag = 0
            dist += 1

        direction += 1
        if direction >= 4:
            direction = 0

print(answer)
