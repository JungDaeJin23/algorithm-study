# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
def back_tracking(n, row):
    global ans, used_coordinate
    if row == n:
        ans += 1
        return

    for col in range(n):
        if promising(row, col):
            used_coordinate.append((row, col))
            back_tracking(n, row+1)
            used_coordinate.pop(-1)
    return


def promising(row, col):
    global used_coordinate
    for used_row, used_col in used_coordinate:
        # 행 검사 생략
        if used_col == col or used_col + used_row == row + col or row - used_row == col - used_col:
            return False
    return True


N = int(input())
ans = 0
used_coordinate = list()
back_tracking(N, 0)
print(ans)