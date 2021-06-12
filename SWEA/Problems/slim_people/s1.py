T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def spread_smell(arr):
    global dr, dc
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                stack = list()
                stack.append((i, j))
                while stack:
                    row, col = stack.pop(-1)
                    for d in range(4):
                        nr = row + dr[d]
                        nc = col + dc[d]
                        if nr < 0 or nr >= len(arr) or nc < 0 or nc >= len(arr[i]):
                            continue
                        if arr[nr][nc] == 0:
                            stack.append((nr, nc))
                            arr[nr][nc] = 2

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                cnt += 1

    return cnt


def set_difuser(cnt=0, idx=0):
    global matrix, max_num

    if cnt == 3:
        duplicated_matrix = []
        for i in range(len(matrix)):
            duplicated_matrix.append(matrix[i][:])
        count = spread_smell(duplicated_matrix)
        if count > max_num:
            max_num = count
        return
    else:
        for i in range(idx, len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    set_difuser(cnt=cnt+1, idx=i)
                    matrix[i][j] = 0


for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    set_difuser()

    print('#{0} {1}'.format(tc,max_num))
