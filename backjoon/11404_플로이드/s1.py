# n <= 100 N ** 3 == 10 ** 6 < 10 ** 8 (1 sec)
n = int(input())
m = int(input())
# min(graph[row][col], graph[row][k] + graph[k][col]) 따라서 inf > 200000 틀림 for loop 최대 100
# inf > 100000 * 100
INF = int(1e9)
graph = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    graph[a][b] = min(c, graph[a][b])

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for row in range(n):
        for col in range(n):
            graph[row][col] = min(graph[row][col], graph[row][k] + graph[k][col])


for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i], sep=' ')
