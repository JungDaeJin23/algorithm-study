N = int(input())
M = int(input())
cost_arr = [100000*N] * (N+1)
visited = [0] * (N+1)
visited[0] = 1
graph = [[] for _ in range(N+1)]
# start, goal, cost
for _ in range(M):
    s, g, c = map(int, input().split())
    graph[s].append((g, c))
S, G = map(int, input().split())
cost_arr[S] = 0
visited[S] = 1


def Dikjkstra(graph, node):
    global cost_arr, N
    while True:
        for g, c in graph[node]:
            if cost_arr[node] + c < cost_arr[g]:
                cost_arr[g] = cost_arr[node] + c
        tmp = 100000*N
        min_idx = -1
        for i in range(1, N+1):
            if not visited[i] and cost_arr[i] < tmp:
                tmp = cost_arr[i]
                min_idx = i

        if min_idx == -1:
            break
        visited[min_idx] = 1
        node = min_idx
Dikjkstra(graph, S)
print(cost_arr[G])