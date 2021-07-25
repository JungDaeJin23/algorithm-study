# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다.
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
# 연쇄가 몇 번 연속으로 일어날지 계산

# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
board = [list(input()) for _ in range(12)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
ans = 0


def gravity():
    global board
    row = 10
    while row >= 0:
        for col in range(6):
            below_row = row + 1
            while below_row < 12 and board[below_row][col] == '.':
                below_row += 1
            below_row -= 1
            board[row][col], board[below_row][col] = board[below_row][col], board[row][col]
        row -= 1


def BFS(row, col):
    global dr, dc, board, visited
    puyo = board[row][col]
    queue = [(row, col)]
    idx = 0
    visited[row][col] = True
    while idx < len(queue):
        row, col = queue[idx]
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < 12 and 0 <= nc < 6 and board[nr][nc] == puyo and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True
        idx += 1

    return queue


while True:
    visited = [[False] * 6 for _ in range(12)]
    coordinates = []
    for row in range(12):
        for col in range(6):
            if board[row][col] != '.' and not visited[row][col]:
                tmp = BFS(row, col)
                if len(tmp) >= 4:
                    coordinates.extend(tmp)

    if coordinates:
        for r, c in coordinates:
            board[r][c] = '.'
        ans += 1
    else:
        break
    gravity()

print(ans)