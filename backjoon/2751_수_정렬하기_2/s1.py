# merge sort
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))


def merge_sort(arr, start, end):
    if end - start <= 1:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return arr[start:end+1]
    middle = (start+end)//2
    left_arr = merge_sort(arr, start, middle)
    right_arr = merge_sort(arr, middle+1, end)
    left_idx = 0
    right_idx = 0
    merged_arr = []
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
    if left_idx < len(left_arr):
        merged_arr.extend(left_arr[left_idx:])
    else:
        merged_arr.extend(right_arr[right_idx:])
    return merged_arr


nums = merge_sort(nums, 0, len(nums)-1)
for num in nums:
    print(num)