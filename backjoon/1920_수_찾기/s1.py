N = int(input())
# 모든 정수의 범위는 -2 ** 31 보다 크거나 같고 2 ** 31보다 작다. -> counting 불가
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))
# 1. brute force 10 ** 5 * 10 ** 5 == 10 ** 10
# for idx in range(len(X)):
#     for jdx in range(len(A)):
#         if X[idx] == A[jdx]:
#             print(1)
#             break


# merge sort and binary search
def merge_sort(arr, start, end):
    if end - start == 0:
        return [arr[start]]
    if end - start == 1:
        if arr[start] <= arr[end]:
            return arr[start:end+1]
        return [arr[end], arr[start]]

    middle = (start + end) // 2
    left = merge_sort(arr, start, middle)
    right = merge_sort(arr, middle+1, end)
    left_idx = 0
    right_idx = 0
    new_arr = [0] * (len(left) + len(right))
    new_idx = 0
    while True:
        if left_idx == len(left):
            while right_idx < len(right):
                new_arr[new_idx] = right[right_idx]
                new_idx += 1
                right_idx += 1
            break
        if right_idx == len(right):
            while left_idx < len(left):
                new_arr[new_idx] = left[left_idx]
                new_idx += 1
                left_idx += 1
            break
        if left[left_idx] <= right[right_idx]:
            new_arr[new_idx] = left[left_idx]
            left_idx += 1
            new_idx += 1
        else:
            new_arr[new_idx] = right[right_idx]
            right_idx += 1
            new_idx += 1

    return new_arr


sorted_A = merge_sort(A, 0, len(A)-1)


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    middle = (end + start) // 2
    if arr[middle] == target:
        return 1
    if arr[middle] < target:
        return binary_search(arr, target, middle+1, end)
    return binary_search(arr, target, start, middle-1)


for num in X:
    print(binary_search(sorted_A, num, 0, len(sorted_A) - 1))