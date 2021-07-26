N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# 1. grid
before_color = -1
for house_idx in range(len(cost)-1):
    min_idx = 0
    second_min_idx = -1
    idx = 1
    while idx < len(cost[house_idx]):
        if cost[house_idx][idx] < cost[house_idx][min_idx]:
            second_min_idx = min_idx
            min_idx = idx
        else:
            if second_min_idx == -1:
                second_min_idx = idx
            else:
                if cost[house_idx][idx] < cost[house_idx][second_min_idx]:
                    second_min_idx = idx

        idx += 1

    for rgb_idx in range(len(cost[house_idx])):
        if min_idx == rgb_idx:
            cost[house_idx+1][rgb_idx] += cost[house_idx][second_min_idx]
        else:
            cost[house_idx+1][rgb_idx] += cost[house_idx][min_idx]

print(min(cost[-1]))