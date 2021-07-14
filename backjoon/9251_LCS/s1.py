# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 1. brute force
# 최대 1000글자로 이루어져 있다 2 ** 1000 최대 조합
# bcdefgha
# acdefghb
str1 = input()
str2 = input()
if len(str1) < len(str2):
    shorter_one = str1
    longer_one = str2
else:
    shorter_one = str2
    longer_one = str1
LCS_length = 0


def backtracking(short, long, i=0, j=0, cnt=0):
    global LCS_length
    for idx in range(i, len(short)):
        if cnt + len(short) - idx - 1 < LCS_length:
            break
        for jdx in range(j, len(long)):
            if cnt + len(long) - jdx - 1 < LCS_length:
                break
            if short[idx] == long[jdx]:
                backtracking(short, long, i=idx+1, j=jdx+1, cnt=cnt+1)
    if LCS_length < cnt:
        LCS_length = cnt


backtracking(shorter_one, longer_one)
print(LCS_length)