T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(queue, level=1):
    global ans, maze, start, dr, dc, N
    if level == 0:
        ans = 0
        return
    new_level = 0
    ans += 1
    for i in range(level):
        row, col = queue.pop(0)
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    ans -= 1
                    return
                new_level += 1
                queue.append((nr, nc))
                maze[nr][nc] = 1
    BFS(queue, level=new_level)


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    start = (-1, -1)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start != (-1, -1):
            break

    BFS([start])
    print('#{0} {1}'.format(tc, ans))