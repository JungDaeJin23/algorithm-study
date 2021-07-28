N = int(input())
stack = [0, 1, 1]
while len(stack) <= 10**6:
    n = len(stack)+1
    tmp = [stack[n-2]]
    if n % 3 == 0:
        tmp.append(stack[n//3 - 1])
    if n % 2 == 0:
        tmp.append(stack[n//2-1])
    stack.append(min(tmp)+1)
print(stack[N-1])