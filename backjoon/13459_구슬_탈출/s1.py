N, M = map(int, input().split())
Board = [list(input()) for _ in range(N)]

r_flag = False
b_flag = False
red_position = (0, 0)
blue_position = (0, 0)
for row in range(N):
    for col in range(M):
        if Board[row][col] == 'R':
            red_position = (row, col)
            r_flag = True
        elif Board[row][col] == 'B':
            blue_position = (row, col)
            b_flag = True
    if r_flag and b_flag:
        break

answer = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def sol(r, b, board, count=0):
    global answer, dr, dc, N, M
    if count == 10 or answer == 1:
        return

    priority = 'red'
    for d in range(4):
        duplicated_board = []
        for i in range(N):
            duplicated_board.append(board[i][:])
        if dc[d] and r[0] == b[0]:
            if dc[d] == 1 and b[1] > r[1]:
                priority = 'blue'
            elif dc[d] == -1 and b[1] < r[1]:
                priority = 'blue'
        elif dr[d] and r[1] == b[1]:
            if dr[d] == 1 and b[0] > r[0]:
                priority = 'blue'
            elif dr[d] == -1 and b[0] < r[0]:
                priority = 'blue'
        moved_r = r
        moved_b = b
        fail_flag = False
        if priority == 'red':
            while True:
                nr = moved_r[0] + dr[d]
                nc = moved_r[1] + dc[d]
                if duplicated_board[nr][nc] == '#' or duplicated_board[nr][nc] == 'B':
                    break
                elif duplicated_board[nr][nc] == 'O':
                    duplicated_board[moved_r[0]][moved_r[1]] = '.'
                    answer = 1
                    break
                else:
                    duplicated_board[moved_r[0]][moved_r[1]] = '.'
                    moved_r = (nr, nc)
                    duplicated_board[moved_r[0]][moved_r[1]] = 'R'
            while True:
                nr = moved_b[0] + dr[d]
                nc = moved_b[1] + dc[d]
                if duplicated_board[nr][nc] == '#' or duplicated_board[nr][nc] == 'R':
                    break
                elif duplicated_board[nr][nc] == 'O':
                    duplicated_board[moved_b[0]][moved_b[1]] = '.'
                    answer = 0
                    fail_flag = True
                    break
                else:
                    duplicated_board[moved_b[0]][moved_b[1]] = '.'
                    moved_b = (nr, nc)
                    duplicated_board[moved_b[0]][moved_b[1]] = 'B'
        else:
            while True:
                nr = moved_b[0] + dr[d]
                nc = moved_b[1] + dc[d]
                if duplicated_board[nr][nc] == '#' or duplicated_board[nr][nc] == 'B':
                    break
                elif duplicated_board[nr][nc] == 'O':
                    duplicated_board[moved_b[0]][moved_b[1]] = '.'
                    answer = 0
                    fail_flag = True
                    break
                else:
                    duplicated_board[moved_b[0]][moved_b[1]] = '.'
                    moved_b = (nr, nc)
                    duplicated_board[moved_b[0]][moved_b[1]] = 'B'
            while True:
                nr = moved_r[0] + dr[d]
                nc = moved_r[1] + dc[d]
                if duplicated_board[nr][nc] == '#' or duplicated_board[nr][nc] == 'R':
                    break
                elif duplicated_board[nr][nc] == 'O':
                    duplicated_board[moved_r[0]][moved_r[1]] = '.'
                    answer = 1
                    break
                else:
                    duplicated_board[moved_r[0]][moved_r[1]] = '.'
                    moved_r = (nr, nc)
                    duplicated_board[moved_r[0]][moved_r[1]] = 'R'
        if fail_flag:
            continue
        sol(moved_r, moved_b, duplicated_board, count=count+1)
        if answer:
            return


sol(red_position, blue_position, Board)
print(answer)
