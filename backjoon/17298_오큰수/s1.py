N = int(input())
arr = list(map(int, input().split()))
nge = [-1] * N
# 1. brute force
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             nge[i] = arr[j]
#             break
# print(*nge)

# stack
stack = [0] * N
top = -1
for idx in range(len(arr)):
    if top == -1:
        top += 1
        stack[top] = idx
    else:
        while top != -1:
            tmp_idx = stack[top]
            if arr[tmp_idx] >= arr[idx]:
                top += 1
                stack[top] = idx
                break
            else:
                nge[tmp_idx] = arr[idx]
                top -= 1
        else:
            top += 1
            stack[top] = idx
print(*nge)