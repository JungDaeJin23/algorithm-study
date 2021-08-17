N = int(input())
M = int(input())
cost_arr = [0] * (N+1)
visited = [0] * (N+1)
# start, goal, cost
bus_info = [list(map(int, input().split())) for _ in range(M)]
S, G = map(int, input().split())
visited[S] = 1
node = S
idx = 0
while bus_info:
    s, g, c = bus_info[idx]
    if node == s:
        if cost_arr[g] == 0:
            cost_arr[g] = c + cost_arr[s]
        else:
            tmp = c + cost_arr[s]
            if cost_arr[g] > tmp:
                cost_arr[g] = tmp
        bus_info.pop(idx)
        if idx >= len(bus_info):
            idx = 0
            min_cost = 100000
            min_i = 0
            for i in range(len(visited)):
                if not visited[i] and cost_arr[i] != 0 and cost_arr[i] < min_cost:
                    min_i = i
                    min_cost = cost_arr[i]
            visited[min_i] = 1
            node = min_i
        continue
    idx += 1
    if idx >= len(bus_info):
        idx = 0
        min_cost = 100000
        min_i = 0
        for i in range(len(visited)):
            if not visited[i] and cost_arr[i] != 0 and cost_arr[i] < min_cost:
                min_i = i
                min_cost = cost_arr[i]
        visited[min_i] = 1
        node = min_i

print(cost_arr[G])