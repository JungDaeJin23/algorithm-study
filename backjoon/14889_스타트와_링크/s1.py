from itertools import combinations
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 100 * N
b = list(combinations(range(1, N+1), N//2))
for i in range(N):
    for j in range(i+1, N):
        board[i][j] += board[j][i]
idx = 0
boundary = len(b)//2
while idx < boundary:
    c = combinations(b[idx], 2)
    tmp1 = 0
    for i, j in c:
        tmp1 += board[i-1][j-1]
    tmp2 = 0
    c = combinations(b[len(b)-1-idx], 2)
    for i, j in c:
        tmp2 += board[i-1][j-1]
    tmp3 = abs(tmp1 - tmp2)
    if tmp3 < ans:
        ans = tmp3
    idx += 1
print(ans)