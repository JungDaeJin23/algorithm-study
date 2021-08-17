N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
cost_arr = [987654321] * (N + 1)
visited = [0] * (N + 1)
for _ in range(M):
    s, g = map(int, input().split())
    graph[s].append(g)

cost_arr[X] = 0
while sum(visited) < N:
    min_idx = 0
    min_cost = 987654321
    for idx in range(len(cost_arr)):
        if not visited[idx] and cost_arr[idx] < min_cost:
            min_idx = idx
            min_cost = cost_arr[idx]

    visited[min_idx] = 1
