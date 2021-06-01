T = int(input())

for tc in range(1, T+1):
    # array size
    N = int(input())
    # 1 ≤ each elements in arr_i≤ 1000000
    arr_i = list(map(int, input().split()))
    min_val = max_val = arr_i[0]

    idx = 1
    while idx < len(arr_i):
        if arr_i[idx] > max_val:
            max_val = arr_i[idx]
        elif arr_i[idx] < min_val:
            min_val = arr_i[idx]
        idx += 1

    print('#{0} {1}'.format(tc, max_val-min_val))

# 2, 3, 4, 5, 6 ascending 으로 값이 증가할 경우 if elif 사용불가
# min_val = 1000000
# max_val = 1
#
# idx = 0
# while idx < len(arr_i):
#     if arr_i[idx] > max_val:
#         max_val = arr_i[idx]
#     if arr_i[idx] < min_val:
#         min_val = arr_i[idx]
#     idx += 1
