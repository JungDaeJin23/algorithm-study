# 2에서 출발해서 0인 통로를 따라 이동하며 3에 도착할 수 있는지 확인
T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(start, goal):
    global matrix, dr, dc
    stack = [start]

    while stack:
        row, col = stack.pop(-1)
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if matrix[nr][nc] == goal:
                return 1
            elif matrix[nr][nc] == 0:
                matrix[nr][nc] = 1
                stack.append((nr, nc))
    return 0


for tc in range(1, T+1):
    N = int(input())
    start = (-1, -1)
    goal = 3
    matrix = []
    for i in range(N):
        tmp = list(map(int, input()))
        matrix.append(tmp)
        if start == (-1, -1):
            for j in range(N):
                if tmp[j] in [2, 3]:
                    start = (i, j)
                    goal = tmp[j] + 1 if tmp[j] == 2 else tmp[j] - 1

    print('#{0} {1}'.format(tc, DFS(start, goal)))
