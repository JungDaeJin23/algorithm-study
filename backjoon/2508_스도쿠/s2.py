# Blank express zero
sudoku = [list(map(int, input().split())) for _ in range(9)]


# backtracking
def backtracking(idx=0):
    global sudoku, used_row, used_col, used_box, blank_position, flag
    if idx == len(blank_position):
        flag = True
        return

    row, col = blank_position[idx]
    for num in range(1, 10):
        if used_row[row][num] or used_col[col][num] or used_box[(row//3)*3 + col//3][num]:
            continue
        sudoku[row][col] = num
        used_row[row][num] = 1
        used_col[col][num] = 1
        used_box[(row // 3) * 3 + col // 3][num] = 1

        backtracking(idx=idx+1)
        if flag:
            return

        sudoku[row][col] = 0
        used_row[row][num] = 0
        used_col[col][num] = 0
        used_box[(row // 3) * 3 + col // 3][num] = 0


flag = False
blank_position = []
used_row = [[0]*10 for _ in range(9)]
used_col = [[0]*10 for _ in range(9)]
used_box = [[0]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank_position.append((i, j))
            continue
        # 1.row
        used_row[i][sudoku[i][j]] = 1
        # 2. col
        used_col[i][sudoku[j][i]] = 1
        # 3. box
        used_box[i][sudoku[(i//3)*3 + j//3][(i % 3)*3 + j % 3]] = 1

backtracking(0)
for i in range(9):
    print(*sudoku[i])