N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다.
# 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현한다.
# |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)를 인접한 칸

# 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
#  임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. -> 인접 조건을 따른다.

# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록,
#  그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.

# auto play
# 1. 크기가 가장 큰 블록 그룹을 찾는다.
# 1.1.그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
# 1.2.그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을
# 1.3. , 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
# 3. 격자에 중력이 작용한다
# 4. 격자가 90도 반시계 방향으로 회전한다.
# 5. 다시 격자에 중력이 작용한다.
# 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.
# 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
# size, magic, row, col
criterion = (0, 0, -1, -1)


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
    criterion = (0, 0, -1, -1)
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