import sys
input = sys.stdin.readline
T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c):
    global dr, dc, cq, front, rear, M, N, field
    rear += 1
    # if rear >= boundary:
    #     rear = 0
    # rear = (rear + 1) % boundary
    cq[rear] = (r, c)
    # visited
    field[r][c] = 0
    while rear != front:
        front += 1
        # if front >= boundary:
        #     front = 0
        row, col = cq[front]
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1:
                rear += 1
                # if rear >= boundary:
                #     rear = 0
                cq[rear] = (nr, nc)
                field[nr][nc] = 0


for _ in range(T):
    # M: width, N: height, K: number of cabbages
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    # 두 배추의 위치가 같은 경우는 없다.
    # 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
    # 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
    # 인접 : |r1 - r2| + |c1 - c2| <= 1
    boundary = M * N + 1
    cq = [(-1, -1)] * boundary
    front = 0
    rear = 0

    for _ in range(K):
        # Caution! K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
        col, row = map(int, input().split())
        field[row][col] = 1

    cnt = 0
    for row in range(N):
        for col in range(M):
            if field[row][col] == 1:
                cnt += 1
                BFS(row, col)
    print(cnt)
