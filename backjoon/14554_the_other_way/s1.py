import heapq
N, M, S, E = map(int, input().split())
S -= 1
E -= 1
# N_max * C_max
INF = int(1e15)
graph = [[(INF, 1)] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = (0, 1)
for _ in range(M):
    # 양방향 Bidirectional, (단방향Unidirectional)
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if graph[A][B][0] > C:
        graph[A][B] = (C, 1)
        graph[B][A] = (C, 1)
    elif graph[A][B][0] == C:
        graph[A][B] = (graph[A][B][0], graph[A][B][1] + 1)
        graph[B][A] = (graph[B][A][0], graph[B][A][1] + 1)

dist = [INF] * N
dist[S] = 0
