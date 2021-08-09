N, M, T = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]


def BFS(board):
    global N, M, T
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]
    queue = [(0, 0, 0)]
    visited[0][0] = 1
    level = 1
    tmp = 1
    gram_ans = T+1
    cnt = -1
    while queue:
        cnt += 1
        level = tmp
        tmp = 0
        for _ in range(level):
            row, col, gram = queue.pop(0)
            if row == N - 1 and col == M - 1:
                if gram_ans < cnt:
                    cnt = gram_ans
                if cnt > T:
                    cnt = 'Fail'
                return cnt
            if gram:
                gram_ans = cnt + N - (row + 1) + M - (col + 1)
                continue
            for d in range(4):
                nr = row + dr[d]
                nc = col + dc[d]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] != 1:
                    tmp += 1
                    queue.append((nr, nc, board[nr][nc]))
                    visited[nr][nc] = 1
    if gram_ans <= T:
        return gram_ans
    return "Fail"


ans = BFS(Board)
print(ans)