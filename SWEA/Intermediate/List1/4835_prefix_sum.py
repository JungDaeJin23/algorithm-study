T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = M
    max_prefix_sum = min_prefix_sum = prefix_sum = sum(arr[:M])
    while idx < len(arr):
        # 옛날에는 구간합 매번 반복돌려서 합을 구했다.
        prefix_sum = prefix_sum + arr[idx] - arr[idx-M]
        if max_prefix_sum < prefix_sum:
            max_prefix_sum = prefix_sum
        elif min_prefix_sum > prefix_sum:
            min_prefix_sum = prefix_sum
        idx += 1

    print("#{0} {1}".format(tc, max_prefix_sum - min_prefix_sum))
