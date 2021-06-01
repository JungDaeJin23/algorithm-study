# len(A) = N, int K
# brute force
N, K = map(int, input().split())
A = list(map(int, input().split()))

# time over
# cnt = 0
# for i in range(0, len(A)):
#     for j in range(i + 1, len(A)):
#         for k in range(j + 1, len(A)):
#             if A[i] * A[j] * A[k] % K == 0:
#                 cnt += 1
# print(cnt)

# memoization
# cnt = 0
# for i in range(0, len(A) - 2):
#     if A[i] % K == 0:
#         cnt += (len(A) - i - 1) * (len(A) - i - 2)
#     else:
#         for j in range(i + 1, len(A) - 1):
#             if A[i] * A[j] % K == 0:
#                 cnt += (len(A) - j - 1)
#             else:
#                 for k in range(j + 1, len(A)):
#                     if A[i] * A[j] * A[k] % K == 0:
#                         cnt += 1
# print(cnt)

# memoization + plus
# divided_list = [False] * N
# for idx in range(N):
#     if A[idx] % K == 0:
#         divided_list[idx] = True
#
# cnt = 0
# for i in range(0, len(A) - 2):
#     # if A[i] % K == 0:
#     if divided_list[i]:
#         cnt += (len(A) - i - 1) * (len(A) - i - 2)
#     else:
#         for j in range(i + 1, len(A) - 1):
#             tmp = A[i] * A[j]
#             if divided_list[j]:
#                 cnt += (len(A) - j - 1)
#             elif tmp % K == 0:
#                 cnt += (len(A) - j - 1)
#             else:
#                 for k in range(j + 1, len(A)):
#                     if divided_list[k]:
#                         cnt += 1
#                     elif tmp * A[k] % K == 0:
#                         cnt += 1
# print(cnt)


# memoization + gcd
def my_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


gcd_list = [0] * N
for idx in range(N):
    gcd_list[idx] = my_gcd(A[idx], K)

cnt = 0
for i in range(0, len(A) - 2):
    if gcd_list[i] == K:
        cnt += (len(A) - i - 1) * (len(A) - i - 2)
    else:
        for j in range(i + 1, len(A) - 1):
            if gcd_list[j] == K:
                cnt += (len(A) - j - 1)
            else:
                tmp = gcd_list[i] * gcd_list[j]
                if tmp == K:
                    cnt += (len(A) - j - 1)
                else:
                    for k in range(j + 1, len(A)):
                        if gcd_list[k] == K:
                            cnt += 1
                        elif tmp * gcd_list[k] == K:
                            cnt += 1
print(cnt)
