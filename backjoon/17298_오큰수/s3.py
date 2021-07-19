# 뒤에서 부터 다른 사람 풀이
import sys
input = sys.stdin.readline

def check(li):
    res = [0]*len(li)
    stack = []
    for i in range(len(li)-1,-1,-1):
        while stack and stack[-1] <= li[i]:
            stack.pop()
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(li[i])
    return res

N = int(input())
arr = list(map(int,input().split()))
res = check(arr)
print(' '.join(map(str,res)))