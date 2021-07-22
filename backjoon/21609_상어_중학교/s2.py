N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0


def BFS(queue, block):
    global dr, dc, board, N
    cnt = 0
    magic_block_cnt = 0
    while queue:
        row, col = queue.pop(0)
        cnt += 1
        if board[row][col] == 0:
            magic_block_cnt += 1
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not counted[nr][nc] and (board[nr][nc] == block or board[nr][nc] == 0):
                queue.append((nr, nc))
                counted[nr][nc] = True
    return cnt, magic_block_cnt


def find_biggest_blocks():
    global board, N, counted, criterion
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not counted[i][j]:
                counted[i][j] = True
                cnt, magic_block_cnt = BFS([(i, j)], board[i][j])
                if cnt > criterion[0]:
                    criterion = (cnt, magic_block_cnt, i, j)
                elif cnt == criterion[0]:
                    if magic_block_cnt > criterion[1]:
                        criterion = (cnt, magic_block_cnt, i, j)
                    elif magic_block_cnt == criterion[1]:
                        if i > criterion[2]:
                            criterion = (cnt, magic_block_cnt, i, j)
                        elif i == criterion[2]:
                            if j > criterion[3]:
                                criterion = (cnt, magic_block_cnt, i, j)
                # 무지개 블록 초기화
                if magic_block_cnt > 0:
                    for i in range(N):
                        for j in range(N):
                            if board[i][j] == 0:
                                counted[i][j] = False


def delete_blocks(queue, block):
    global dr, dc, board, N
    board[queue[0][0]][queue[0][1]] = -2
    while queue:
        row, col = queue.pop(0)
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < N and (board[nr][nc] == block or board[nr][nc] == 0):
                queue.append((nr, nc))
                board[nr][nc] = -2


def gravity():
    global board
    i = N-2
    while i >= 0:
        for j in range(N):
            if board[i][j] >= 0:
                down_i = i+1
                while down_i < N and board[down_i][j] == -2:
                    down_i += 1
                down_i -= 1
                board[i][j], board[down_i][j] = board[down_i][j], board[i][j]
        i -= 1


def turn_anti_clockwise():
    global N, board
    new_board = []
    j = N-1
    while j >= 0:
        tmp = []
        i = 0
        while i < N:
            tmp.append(board[i][j])
            i += 1
        new_board.append(tmp)
        j -= 1
    return new_board


while True:
    # size, magic, row, col
    criterion = (1, 0, -1, -1)
    counted = [[False] * N for _ in range(N)]
    find_biggest_blocks()
    if criterion[0] < 2:
        break
    ans += criterion[0]**2
    i, j = criterion[2: 4]
    delete_blocks([(i, j)], board[i][j])
    gravity()
    board = turn_anti_clockwise()
    gravity()

print(ans)