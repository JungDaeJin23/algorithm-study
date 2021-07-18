# https://rebas.kr/762
sudoku = [list(map(int, input().split())) for _ in range(9)]


# backtracking
def backtracking(idx=0):
    global sudoku, used_row, used_col, used_box, blank_position, n
    if idx == n:
        for i in range(9):
            print(' '.join(map(str, sudoku[i])))
        exit(0)

    row, col = b[idx] // 9, b[idx] % 9
    for num in range(1, 10):
        if not (used_row[row][num] or used_col[col][num] or used_box[(row//3)*3 + col//3][num]):
            sudoku[row][col] = num
            used_row[row][num] = used_col[col][num] = used_box[(row // 3) * 3 + col // 3][num] = 1

            backtracking(idx=idx+1)

            sudoku[row][col] = 0
            used_row[row][num] = used_col[col][num] = used_box[(row // 3) * 3 + col // 3][num] = 0


b, n = [0]*81, 0
used_row = [[0]*10 for _ in range(9)]
used_col = [[0]*10 for _ in range(9)]
used_box = [[0]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            b[n] = i * 9 + j
            n += 1
        else:
            used_row[i][sudoku[i][j]] = 1
            used_col[j][sudoku[i][j]] = 1
            used_box[(i // 3) * 3 + j // 3][sudoku[i][j]] = 1

backtracking()