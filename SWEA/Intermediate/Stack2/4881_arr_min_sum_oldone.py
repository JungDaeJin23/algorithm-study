# input and output
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(len(arr)):
        answer += arr[i][i]
    used_j = [False] * len(arr[0])

    def arr_min_sum(arr, min_sum=0, i=0):
        global used_j, answer
        if i == len(arr):
            if min_sum < answer:
                answer = min_sum
            return

        for idx in range(len(arr[i])):
            if not used_j[idx]:
                used_j[idx] = True
                if min_sum < answer:
                    arr_min_sum(arr, min_sum+arr[i][idx], i+1)
                used_j[idx] = False
    arr_min_sum(arr)

    print("#{0} {1}".format(tc, answer))
