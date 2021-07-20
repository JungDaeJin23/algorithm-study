N = int(input())
arr = list(map(int, input().split()))
dp = [1]*len(arr)
for idx in range(len(arr)):
    for jdx in range(idx+1, len(arr)):
        if arr[jdx] > arr[idx] and dp[jdx] <= dp[idx]:
            dp[jdx] = dp[idx] + 1
print(max(dp))