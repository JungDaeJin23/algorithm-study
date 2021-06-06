def DFS_recursion(node, goal):
    global edges, visited
    visited[node] = True
    tmp = 0
    if node == goal:
        return 1

    for next_node in edges[node]:
        if not visited[next_node]:
            tmp += DFS_recursion(next_node, goal)
    return tmp

def DFS_iteration(start, goal):
    global edges, visited
    stack = [start]

    while stack:
        node = stack.pop(-1)
        for vertex in edges[node]:
            if not visited[vertex]:
                if vertex == goal:
                    return 1
                stack.append(vertex)
                visited[vertex] = True
    return 0


T = int(input())
# 노드번호는 1번부터 V까지 존재
# 방향성 그래프
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        node1, node2 = map(int, input().split())
        edges[node1].append(node2)
    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    # answer = DFS_iteration(S, G)
    answer = DFS_recursion(S, G)
    print('#{0} {1}'.format(tc, answer))
