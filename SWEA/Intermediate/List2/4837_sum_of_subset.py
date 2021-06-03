# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
T = int(input())
A = [i for i in range(1, 13)]


def get_subset(arr, count, k, total=0, el_count=0, start_idx=0):
    global cnt
    if el_count == count:
        if total == k:
            cnt += 1
        return

    for idx in range(start_idx, len(arr)):
        get_subset(arr, count, k, total=total+arr[idx], el_count=el_count+1, start_idx=idx+1)

for tc in range(1, T+1):
    cnt = 0
    N, K = map(int, input().split())
    get_subset(A, N, K)
    print('#{0} {1}'.format(tc, cnt))
