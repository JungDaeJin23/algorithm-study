R, C, T = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_upper_air_cleaner(board):
    global R
    col = 0
    row = 2
    while board[row][col] != -1:
        row += 1

    return row


def diffusion(board):
    global dr, dc, R, C
    diffused_board = [[0] * C for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if board[row][col] <= 0:
                continue
            diffusion_value = board[row][col] // 5
            cnt = 0
            for d in range(4):
                nr = row + dr[d]
                nc = col + dc[d]
                if nr < 0 or nr >= R or nc < 0 or nc >= C or board[nr][nc] == -1:
                    continue
                cnt += 1
                diffused_board[nr][nc] += diffusion_value
            diffused_board[row][col] += board[row][col] - diffusion_value * cnt

    return diffused_board


def air_cleaner(board, row):
    global R, C
    tmp = 0
    # 첫번째 우측으로 이동
    for col in range(1, C):
        board[row][col], tmp = tmp, board[row][col]
    # 두번째 위로 이동
    col = C-1
    for r in range(row-1, -1, -1):
        board[r][col], tmp = tmp, board[r][col]
    # 세번째 좌로 이동
    for col in range(C-2, -1, -1):
        board[0][col], tmp = tmp, board[0][col]
    # 네번째 아래로 이동
    col = 0
    for r in range(1, row):
        board[r][col], tmp = tmp, board[r][col]

    tmp = 0
    row += 1
    # 첫번째 우측으로 이동
    for col in range(1, C):
        board[row][col], tmp = tmp, board[row][col]
    # 두번째 아래로 이동
    col = C - 1
    for r in range(row+1, R):
        board[r][col], tmp = tmp, board[r][col]
    # 세번째 좌로 이동
    for col in range(C-2, -1, -1):
        board[R-1][col], tmp = tmp, board[R-1][col]
    # 네번째 위로 이동
    col = 0
    for r in range(R-2, row, -1):
        board[r][col], tmp = tmp, board[r][col]

    return board


upper_air_cleaner_position_row = find_upper_air_cleaner(Board)

for _ in range(T):
    Board = diffusion(Board)
    Board[upper_air_cleaner_position_row][0] = -1
    Board[upper_air_cleaner_position_row+1][0] = -1
    Board = air_cleaner(Board, upper_air_cleaner_position_row)

ans = 2
for i in range(R):
    ans += sum(Board[i])

print(ans)