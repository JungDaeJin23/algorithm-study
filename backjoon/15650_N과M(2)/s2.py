N, M = map(int, input().split())
stack = [0] * M


def backtracking(n, m, stack, top=-1, start=1):
    if top + 1 == m:
        print(*stack)
        return
    for num in range(start, n+1):
        top += 1
        stack[top] = num
        backtracking(n, m, stack, top=top, start=num+1)
        top -= 1
    return


backtracking(N, M, stack)