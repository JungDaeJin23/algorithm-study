

# Adjacency matrix
def make_adjacency_matrix(v, adjacency_info):
    adjacency_matrix = [[0] * (v + 1) for _ in range(v + 1)]
    i = 0
    while i < len(adjacency_info):
        adjacency_matrix[adjacency_info[i]][adjacency_info[i + 1]] = 1
        adjacency_matrix[adjacency_info[i + 1]][adjacency_info[i]] = 1
        i += 2
    return adjacency_matrix


# dfs
def dfs(start, goal, adjacency_matrix):
    stack = [start]
    # adjacency_matrix size is v + 1 by v + 1
    visited = [False] * len(adjacency_matrix)
    visited[start] = True

    while stack:
        if visited[goal]:
            return 1
        v = stack.pop(-1)

        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[v][j] and not visited[j]:
                stack.append(j)
                visited[j] = True
    return 0


def bfs(start, goal, adjacency_matrix):
    stack = [start]
    # adjacency_matrix size is v + 1 by v + 1
    visited = [False] * len(adjacency_matrix)
    visited[start] = True
    d = 0
    n = len(stack)

    while stack:

        v = stack.pop(0)

        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[v][j] and not visited[j]:
                stack.append(j)
                visited[j] = True
        n -= 1
        if n == 0:
            d += 1
            n = len(stack)
            if visited[goal]:
                return d
    return 0


# input and output
T = int(input())
for tc in range(1, T + 1):
    # V: count of node, E: count of edge
    V, E = map(int, input().split())
    # Adjacency_info = [[ ,] , [ , ], ...] X
    # Adjacency_info = [list(map(int, input().split())) for _ in range(E)]
    # Adjacency_info = [N, N, N, N, ...]
    Adjacency_info = [int(node) for _ in range(E) for node in input().split()]
    Adjacency_matrix = make_adjacency_matrix(V, Adjacency_info)
    S, G = map(int, input().split())

    print("#{0} {1}".format(tc, bfs(S, G, Adjacency_matrix)))
