def sol(position, cnt=1):
    global captured, board, dr, dc, N
    if cnt == 4:
        return
    row, col = position
    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            pass
        else:
            continue
        while board[nr][nc] == 0:
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                pass
            else:
                break
        else:
            if board[nr][nc]:
                nnr = nr + dr[d]
                nnc = nc + dc[d]
                while 0 <= nnr < N and 0 <= nnc < N:
                    if board[nnr][nnc]:
                        captured[nnr][nnc] = 1
                        board[nnr][nnc] = 0
                        sol((nnr, nnc), cnt=cnt + 1)
                        board[nnr][nnc] = 1
                        break
                    else:
                        sol((nnr, nnc), cnt=cnt+1)
                    nnr += dr[d]
                    nnc += dc[d]
T = int(input())
# up down left right
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    captured = [[0 for _ in range(N)] for _ in range(N)]
    flag = False
    for row in range(N):
        for col in range(N):
            if board[row][col] == 2:
                board[row][col] = 0
                position = (row, col)
                flag = True
                break
        if flag:
            break
    sol(position)
    answer = 0
    for a in captured:
        answer += sum(a)
    print('#{0} {1}'.format(tc, answer))