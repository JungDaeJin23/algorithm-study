# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000),  (1 ≤ Pi ≤ 1,000)
# 1. brute force
# check every combination and return minimum summation
# 2. counting sort(N)
# 3. sort NlogN



# 2.
boundary = 1000
N = int(input())
counting_list = [0] * (boundary + 1)
A = list(map(int, input().split()))
answer_list = [0 for _ in range(N)]

for idx in A:
    counting_list[idx] += 1

answer = 0
idx = 1
i = 0
# while N:
#     while counting_list[idx]:
#         answer += idx
#         answer_list[i] = answer
#         i += 1
#         N -= 1
#         counting_list[idx] -= 1
#     idx += 1
# print(sum(answer_list)) 72ms
while N:
    while counting_list[idx]:
        answer += idx * N
        N -= 1
        counting_list[idx] -= 1
    idx += 1
print(answer)  # 76ms 왜 더 오래 걸리지..? 곱셈이라?


# 3.
boundary = 1000
N = int(input())
A = sorted(list(map(int, input().split())))

answer = 0

for a in A:
    answer += a * N
    N -= 1

print(answer)  # 88 ms
