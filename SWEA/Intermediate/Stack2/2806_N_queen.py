T = int(input())


def is_promising(i, j):
    global queen_stack
    for row, col in queen_stack:
        if row == i or col == j or i - j == row - col or i + j == row + col:
            return False
    return True


def get_cases(n, i=0):
    global cnt, queen_stack
    if i == n:
        cnt += 1
        return
    for j in range(n):
        if is_promising(i, j):
            queen_stack.append((i, j))
            get_cases(n, i=i+1)
            queen_stack.pop(-1)


for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    queen_stack = []
    get_cases(N)

    print('#{0} {1}'.format(tc, cnt))
