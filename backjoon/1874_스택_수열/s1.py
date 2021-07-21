T = int(input())
stack = [0] * T
target_stack = [int(input()) for _ in range(T)]
target_top = 0
top = -1
ans = ''
num = 1
while num <= T:
    while num <= T and top < len(stack) and (top == -1 or stack[top] != target_stack[target_top]):
        top += 1
        stack[top] = num
        num += 1
        ans += '+'
    while top >= 0 and target_top < len(target_stack) and stack[top] == target_stack[target_top]:
        top -= 1
        target_top += 1
        ans += '-'
if top != -1:
    print('NO')
else:
    print(*ans, sep='\n')