N, M = map(int, input().split())
used = [0] * (N+1)
stack = [0] * M


def backtracking(n, m, stack, top=-1):
    global used
    if top + 1 == m:
        print(*stack)
        return
    for num in range(1, n+1):
        if not used[num]:
            used[num] = 1
            top += 1
            stack[top] = num
            backtracking(n, m, stack, top=top)
            top -= 1
            used[num] = 0
    return


backtracking(N, M, stack)