# can escape?
def have_exit_path(maze):
    # find start or exit point
    point = []
    i = 0
    while i < len(maze) and not point:
        j = 0
        while j < len(maze) and not point:
            if maze[i][j] in [2, 3]:
                    point = [i, j]
                    # visited check
                    maze[i][j] = 1
            j += 1
        i += 1

    route_stack = [[]] * (len(maze) * len(maze[0]))
    top = -1
    # push
    top += 1
    route_stack[top] = point

    while top != -1:
        # delta direction
        # up, right, down ,left
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        # change visited route to wall
        # pop
        row, col = route_stack[top]
        top -= 1
        # if maze[row][col] in [2, 3]:
        #     return 1
        for d in range(len(dr)):
            row += dr[d]
            col += dc[d]
            if 0 <= row < len(maze) and 0 <= col < len(maze[row]) and maze[row][col] != 1:
                # push
                top += 1
                route_stack[top] = [row, col]
                # breakpoint
                if maze[row][col] in [2, 3]:
                    return 1
                # visited check
                maze[row][col] = 1
            # back to original position
            row -= dr[d]
            col -= dc[d]

    return 0


# input and output
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int, list(input()))) for _ in range(N)]
    print("#{0} {1}".format(tc, have_exit_path(Maze)))
