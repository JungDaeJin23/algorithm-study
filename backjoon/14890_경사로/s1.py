# N(2 ≤ N ≤ 100)
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 경사로는 다른 방향의 길을 방해하지 않는다.
tmp = []
ans = 0
# row-major right way
for i in range(N):
    height = board[i][0]
    slope_length = 1
    direction = 1
    for j in range(1, N):
        if height != board[i][j]:
            if board[i][j] == height + 1 and direction == 1 and slope_length >= L:
                height = board[i][j]
                slope_length = 0
            # direction 확인 없어서 연속해서 하강하는 경우 포함 못했음
            elif board[i][j] == height - 1 and direction == 1:
                height = board[i][j]
                direction = -1
                slope_length = 0
            else:
                break
        slope_length += 1
        if direction == -1 and slope_length >= L:
            direction = 1
            slope_length = 0
    else:
        if direction == 1:
            # tmp.append(('i', i))
            ans += 1

# col-major
for j in range(N):
    height = board[0][j]
    slope_length = 1
    direction = 1
    for i in range(1, N):
        if height != board[i][j]:
            if board[i][j] == height + 1 and direction == 1 and slope_length >= L:
                height = board[i][j]
                slope_length = 0
            elif board[i][j] == height - 1 and direction == 1:
                height = board[i][j]
                direction = -1
                slope_length = 0
            else:
                break
        slope_length += 1
        if direction == -1 and slope_length >= L:
            direction = 1
            slope_length = 0
    else:
        if direction == 1:
            ans += 1
            # tmp.append(('j', j))

# print(ans, tmp)
print(ans)