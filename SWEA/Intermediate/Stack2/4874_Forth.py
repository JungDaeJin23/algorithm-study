# 나눗셈의 경우 항상 나누어 떨어진다.
T = int(input())
operator = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x//y}

for tc in range(1, T+1):
    expression = list(input().split())
    answer = 'error'

    stack = [0]*len(expression)
    top = -1

    for el in expression:
        if el == '.':
            if top == 0:
                answer = stack[top]
        elif operator.get(el):
            if top <= 0:
                break
            tmp1 = stack[top]
            top -= 1
            tmp2 = stack[top]
            top -= 1

            ans = operator[el](tmp2, tmp1)
            top += 1
            stack[top] = ans
        else:
            top += 1
            stack[top] = int(el)

    print('#{0} {1}'.format(tc, answer))
