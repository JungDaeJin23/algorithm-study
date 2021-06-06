# 괄호 {}, ()가 제대로 짝을 이뤘는지 검사
T = int(input())
brackets = ['(', ')', '{', '}']
for tc in range(1, T+1):
    str1 = input()
    answer = 0
    stack = [''] * len(str1)
    top = -1
    for character in str1:
        if character in brackets:
            # is empty
            if top == -1:
                if character in ['(', '{']:
                    top += 1
                    stack[top] = character
                else:
                    break
            else:
                if character == ')':
                    if stack[top] == '(':
                        top -= 1
                    else:
                        break
                elif character == '}':
                    if stack[top] == '{':
                        top -= 1
                    else:
                        break
                else:
                    top += 1
                    stack[top] = character
    else:
        if top == -1:
            answer = 1

    print('#{0} {1}'.format(tc, answer))
