import sys
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
cost_arr = [987654321] * (N + 1)
visited = [0] * (N + 1)
ans = []
visited[0] = 1
for _ in range(M):
    s, g = map(int, input().split())
    graph[s].append(g)

visited[X] = 1
cost_arr[X] = 0
for _ in range(N):
    for node in graph[X]:
        if cost_arr[X] + 1 < cost_arr[node]:
            cost_arr[node] = cost_arr[X] + 1
    X = 0
    for node in range(1, N+1):
        if not visited[node] and cost_arr[node] < cost_arr[X]:
            X = node
    visited[X] = 1
    if cost_arr[X] == K:
        break

for idx in range(1, len(cost_arr)):
    if cost_arr[idx] == K:
        ans.append(idx)
if len(ans):
    print(*ans, sep='\n')
else:
    print(-1)

