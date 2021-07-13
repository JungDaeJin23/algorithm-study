import sys
input = sys.stdin.readline

# counting sort 할 때 음수가 있다면 해당 값만큼 범위를 이동한 뒤에 카운트를 시작한다. ex) x - (-30)

N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
print(round(sum(nums)/N))
nums.sort()
print(nums[N//2])
num_dict = dict()
for num in nums:
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1
num_count_list = sorted(num_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
arr = []
for num, cnt in num_count_list:
    if cnt == num_count_list[0][1]:
        arr.append(num)
    else:
        break
if len(arr) == 1:
    print(arr[0])
else:
    print(arr[-2])
print(nums[-1] - nums[0])