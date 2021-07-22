N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(row, col, block):
    global board, N, counted



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