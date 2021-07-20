N = input()
arr = list(map(int, input().split()))
dp = [1]*len(arr)
reversed_dp = [1]*len(arr)
idx = 0
reversed_idx = len(arr)-1
while idx < len(arr):
    jdx = idx+1
    reversed_jdx = reversed_idx - 1
    while jdx < len(arr):
        if arr[idx] < arr[jdx] and dp[idx] >= dp[jdx]:
            dp[jdx] = dp[idx]+1
        jdx += 1
        if arr[reversed_jdx] > arr[reversed_idx] and reversed_dp[reversed_jdx] <= reversed_dp[reversed_idx]:
            reversed_dp[reversed_jdx] = reversed_dp[reversed_idx] + 1
        reversed_jdx -= 1
    idx += 1
    reversed_idx -= 1
# print(dp)
# print(reversed_dp)
for idx in range(len(dp)):
    dp[idx] += reversed_dp[idx]-1
print(max(dp))