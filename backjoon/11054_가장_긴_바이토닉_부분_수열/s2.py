# 틀린 로직
N = input()
arr = list(map(int, input().split()))
dp = [1]*len(arr)
reversed_dp = [1]*len(arr)
idx = 0

while idx < len(arr):
    jdx = idx - 1
    while jdx >= 0:
        if arr[jdx] < arr[idx]:
            dp[idx] += dp[jdx]
            break
        jdx -= 1
    idx += 1

# 함수화 가능하지만 reverse 안하려고 같은 로직을 두 번 작성했다.
reversed_idx = len(arr)-1
while reversed_idx >= 0:
    reversed_jdx = reversed_idx + 1
    while reversed_jdx < len(arr):
        if arr[reversed_idx] < arr[reversed_jdx]:
            reversed_dp[reversed_idx] += reversed_dp[reversed_jdx]
            break
        reversed_jdx += 1
    reversed_idx -= 1
print(dp)
# [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
print(reversed_dp)
# [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]

for idx in range(len(dp)):
    dp[idx] += reversed_dp[idx]-1
print(max(dp))