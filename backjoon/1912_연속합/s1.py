N = int(input())
nums = list(map(int, input().split()))
ans = -1000
tmp = 0

for idx in range(len(nums)):
    tmp += nums[idx]
    if tmp > ans:
        ans = tmp
    if tmp < 0:
        tmp = 0

print(ans)
