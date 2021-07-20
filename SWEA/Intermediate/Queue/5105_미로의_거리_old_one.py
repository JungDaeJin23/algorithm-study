
# N by N size maze
# find the start point and calculate the distance from start to exit point
# 1.make wall, 2, use boundary condition
# bfs


# find the start point
def find_start(maze):
    i = 0
    while i < len(maze):
        j = 0
        while j < len(maze[i]):
            if maze[i][j] == 2:
                return i, j
            j += 1
        i += 1


def bfs(si, sj, maze):
    queue = [(si, sj)]
    dist = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:
        size = len(queue)

        for _ in range(size):
            row, col = queue.pop(0)

            for t in range(len(dr)):
                row += dr[t]
                col += dc[t]
                if 0 <= row < len(maze) and 0 <= col < len(maze[row]):
                    if maze[row][col] == 3:
                        return dist
                    elif maze[row][col] == 0:
                        queue.append((row, col))
                        maze[row][col] = 1
                row -= dr[t]
                col -= dc[t]
        dist += 1
    return 0

# input and output
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int, list(input()))) for _ in range(N)]
    start_i, start_j = find_start(Maze)
    print("#{0} {1}".format(tc, bfs(start_i, start_j, Maze)))
