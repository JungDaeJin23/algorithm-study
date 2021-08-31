def solution(n, weak, dist):
    # weak의 길이는 1 이상 15 이하입니다
    if len(weak) == 1:
        return 1
    dist.sort(reverse=True)

    sep_dist = []
    idx = 0
    while idx < len(weak) - 1:
        sep_dist.append(weak[idx + 1] - weak[idx])
        idx += 1
    sep_dist.append(n + weak[0] - weak[len(weak) - 1])

    cnt = 1
    flag = False
    while True:
        max_idx = 0
        for i in range(len(sep_dist)):
            if sep_dist[i] > sep_dist[max_idx]:
                max_idx = i
        if sep_dist[max_idx] == -1:
            return -1
        sep_dist[max_idx] = -1

        prefix_dist = []
        tmp = 0
        rear = len(sep_dist) - 1
        while sep_dist[rear] != -1:
            tmp += sep_dist[rear]
            rear -= 1
        front = 0
        while front < rear and sep_dist[front] != -1:
            tmp += sep_dist[front]
            front += 1
        prefix_dist.append(tmp)

        tmp = 0
        front += 1
        while front <= rear:
            if sep_dist[front] == -1:
                if tmp != 0:
                    prefix_dist.append(tmp)
                    tmp = 0
            else:
                tmp += sep_dist[front]
            front += 1

        prefix_dist.sort(reverse=True)

        for i in range(cnt):
            if len(prefix_dist) < cnt:
                flag = True
                break
            if prefix_dist[i] > dist[i]:
                break
        else:
            flag = True

        if flag:
            return cnt

        cnt += 1