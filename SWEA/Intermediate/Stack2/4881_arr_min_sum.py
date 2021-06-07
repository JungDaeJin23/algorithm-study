T = int(input())


def get_min_sum(i=0, tmp=0):
    global matrix, min_sum, column_stack, N
    if i == N:
        if tmp < min_sum:
            min_sum = tmp
        return

    j = 0
    while j < N:
        if j not in column_stack:
            temp = tmp + matrix[i][j]
            if temp >= min_sum:
                j += 1
                continue
            column_stack.append(j)
            get_min_sum(i=i+1, tmp=temp)
            column_stack.pop(-1)
        j += 1


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 0
    column_stack = []
    for i in range(N):
        min_sum += matrix[i][i]
    get_min_sum()
    print('#{0} {1}'.format(tc, min_sum))
