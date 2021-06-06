T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = ['']*len(s)
    top = -1

    for character in s:
        if top == -1:
            top += 1
            stack[top] = character
        else:
            if stack[top] == character:
                top -= 1
            else:
                top += 1
                stack[top] = character

    print('#{0} {1}'.format(tc, top+1))
