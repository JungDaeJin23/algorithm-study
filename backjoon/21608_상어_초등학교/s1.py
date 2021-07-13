N = int(input())
wish_list = [list(map(int, input().split())) for _ in range(N**2)]
# 아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.
# [[자신 번호, 좋아하는 번호 1, 2, 3, 4], ...]
# |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.

board = [[0]*N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for wish in wish_list:
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    # row, col, cnt
    info = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                cnt = 0
                blank_cnt = 0
                for d in range(4):
                    nr = row + dr[d]
                    nc = col + dc[d]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    # 숫자가 중복되거나 자기 자신 좋아하는 경우 없음 dont need to wish[1:]
                    if board[nr][nc] in wish:
                        cnt += 1
                    if board[nr][nc] == 0:
                        blank_cnt += 1
                info.append((row, col, cnt, blank_cnt))
    info.sort(key=lambda x: x[2], reverse=True)
    if len(info) == 1 or info[0][2] != info[1][2]:
        row, col, cnt, blank_cnt = info[0]
        board[row][col] = wish[0]
        continue
    info = [info[i] for i in range(len(info)) if info[i][2] == info[0][2]]
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    info.sort(key=lambda x: x[3], reverse=True)
    if len(info) == 1 or info[0][3] != info[1][3]:
        row, col, cnt, blank_cnt = info[0]
        board[row][col] = wish[0]
        continue
    info = [info[i] for i in range(len(info)) if info[i][3] == info[0][3]]
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    info.sort(key=lambda x: x[0])
    if len(info) == 1 or info[0][0] != info[1][0]:
        row, col, cnt, blank_cnt = info[0]
        board[row][col] = wish[0]
        continue

    info = [info[i] for i in range(len(info)) if info[i][0] == info[0][0]]
    info.sort(key=lambda x: x[1])
    # if info[0][1] != info[1][1]:
    row, col, cnt, blank_cnt = info[0]
    board[row][col] = wish[0]
# print(board)

#  그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
#  그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
wish_list.sort(key=lambda x: x[0])
ans = 0
for row in range(N):
    for col in range(N):
        cnt = 0
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc] in wish_list[board[row][col]-1]:
                cnt += 1
        if cnt:
            ans += 10 ** (cnt-1)
print(ans)