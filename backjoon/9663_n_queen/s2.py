# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
def back_tracking(n, row, used):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        for used_row, used_col in used:
            if used_col == col or used_col + used_row == row + col or row - used_row == col - used_col:
                break
        else:
            used.append((row, col))
            back_tracking(n, row+1, used)
            used.pop(-1)
    return


N = int(input())
ans = 0
used_coordinate = list()
back_tracking(N, 0, used_coordinate)
print(ans)