def n_queen(n, i, positions):
    global answer
    if n == i:
        answer += 1
        return

    # backtracking
    for j in range(n):
        # promising
        # 같은 행은 나올리 없음
        flag = True
        for row, col in positions:
            # column, diagonal, reverse diagonal check
            if j == col or i+j == row+col or i-j == row - col:
                flag = False
                break

        if flag:
            positions.append((i, j))
            n_queen(n, i+1, positions)
            positions.pop()

# input and output
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    n_queen(N, 0, [])
    print("#{0} {1}".format(tc, answer))