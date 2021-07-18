# Blank express zero
sudoku = [list(map(int, input().split())) for _ in range(9)]


# backtracking
def backtracking(i):
    global sudoku, cnt
    for row in range(i, 9):
        for col in range(9): # 조건문 넣어서 분기하는니 그냥 돌리자
            if sudoku[row][col] != 0:
                continue
            for num in range(1, 10):
                if not promising(row, col, num):
                    continue
                sudoku[row][col] = num
                cnt -= 1
                if col == 8:
                    backtracking(row+1)
                else:
                    backtracking(row)
                if cnt == 0:
                    return
                sudoku[row][col] = 0
                cnt += 1


# check 3 condition
# 1. row, 2. col, 3. box
def promising(row, col, num):
    global sudoku
    # 1.row
    for j in range(9):
        if sudoku[row][j] == num:
            return False
    # 2. col
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    # 3. box
    start_box_row = (row // 3) * 3
    start_box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            box_row = start_box_row + i
            box_col = start_box_col + j
            if sudoku[box_row][box_col] == num:
                return False
    return True


cnt = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            cnt += 1
backtracking(0)
for i in range(9):
    print(*sudoku[i])