# directed graph
def dfs(start, goal, adjacency_list):
    visited = [False] * (len(adjacency_list))
    stack = [start]
    while stack:
        vertex = stack.pop()
        visited[vertex] = True
        # 재현님 방법 이해했습니다. 이게 더 스택 같네요!
        for linked_vertex in adjacency_list[vertex]:
            if not visited[linked_vertex]:
                stack.append(linked_vertex)
    if visited[goal]:
        return 1
    return 0


# input and output
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # Adjacency_list = [[] * (V + 1)] 잦은 실수 []*10 == []
    Adjacency_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        v_start, v_end = map(int, input().split())
        Adjacency_list[v_start].append(v_end)
    test_v_start, test_v_end = map(int,input().split())
    print("#{0} {1}".format(tc, dfs(test_v_start, test_v_end, Adjacency_list)))
