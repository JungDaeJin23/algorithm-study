N, M = map(int, input().split())
Maze = [list(input()) for _ in range(N)]
# ord('a') == 97, ord('A') == 65
# keys_dict = dict()
# for i in range(N):
#     for j in range(M):
#         if 'a' <= Maze[i][j] <= 'z':
#             if not keys_dict.get(Maze[i][j].upper()):
#                 keys_dict[Maze[i][j].upper()] = 1
# for i in range(N):
#     for j in range(M):
#         if 'A' <= Maze[i][j] <= 'Z':
#             if not keys_dict.get(Maze[i][j]):
#                 Maze[i][j] = '#'
key_door_pair = [0]*26
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 25000000


# 거리를 알아야된다 -> BFS
def BFS(maze, position, keys, cnt=0):
    global dr, dc, N, M, ans
    visited = [[0]*M for _ in range(N)]
    visited[position[0]][position[1]] = 1
    queue = [position]
    scope = 0
    tmp_scope = 1
    while queue:
        scope = tmp_scope
        tmp_scope = 0
        cnt += 1
        for _ in range(scope):
            row, col = queue.pop(0)
            for d in range(4):
                nr = row + dr[d]
                nc = col + dc[d]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] != '#':
                    if maze[nr][nc] == '.':
                        tmp_scope += 1
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                    elif 'a' <= maze[nr][nc] <= 'z':
                        maze[position[0]][position[1]] = '.'
                        keys.append(maze[nr][nc].upper())
                        maze[nr][nc] = '0'
                        BFS(maze, (nr, nc), keys, cnt=cnt)
                        maze[position[0]][position[1]] = '0'
                        maze[nr][nc] = keys.pop(-1).lower()
                    elif maze[nr][nc] in keys:
                        maze[position[0]][position[1]] = '.'
                        tmp, maze[nr][nc] = maze[nr][nc], '0'
                        BFS(maze, (nr, nc), keys, cnt=cnt)
                        maze[position[0]][position[1]] = '0'
                        maze[nr][nc] = tmp
                    elif maze[nr][nc] == '1':
                        if cnt < ans:
                            ans = cnt
                        # return
    return


def find_position(maze):
    global N, M
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '0':
                return i, j


# 한번에 한 이벤트 == 열쇠를 줍는다, 문을 연다. 둘 중 하나의 일만 일어난다.
# 분기가 이벤트를 기준으로 일어난다.
# 아무런 새 이벤트도 발생하지 않는다. -> 탈출 불가 return -1

position = find_position(Maze)
keys = []
BFS(Maze, position, keys)
if ans != 25000000:
    print(ans)
else:
    print(-1)