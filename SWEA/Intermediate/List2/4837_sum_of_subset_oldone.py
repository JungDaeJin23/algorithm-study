def get_sub_set(a):
    for i in range(1 << len(a)):
        sub_set = []
        for j in range(len(a)):
            if i & (1 << j):
                sub_set.append(a[j])
        yield sub_set


def n_size_sub_set2(a, n, k):
    cnt = 0
    for sub_set in get_sub_set(a):
        if len(sub_set) == n and sum(sub_set) == k:
            cnt += 1

    return cnt


# input and output
T = int(input())
A = [i for i in range(1, 13)]
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    print("#{0} {1}".format(tc, n_size_sub_set2(A, N, K)))