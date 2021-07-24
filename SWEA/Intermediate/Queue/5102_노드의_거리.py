def BFS(s, g):
    global V, graph
    visited = [False] * (V+1)
    visited[s] = True
    level = 0
    next_cnt = 1
    q = [s]
    while next_cnt:
        level += 1
        cnt = next_cnt
        next_cnt = 0
        for _ in range(cnt):
            node = q.pop(0)
            for i in range(1, V+1):
                if graph[node][i] and not visited[i]:
                    if i == g:
                        return level
                    q.append(i)
                    visited[i] = True
                    next_cnt += 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V+1)]
    for _ in range(E):
        node1, node2 = map(int, input().split())
        graph[node1][node2] = graph[node2][node1] = 1
    S, G = map(int, input().split())
    print('#{0} {1}'.format(tc, BFS(S, G)))