# Too long explanation..
# input data is balanced parentheses string
# Make it correct parentheses string
# stack? when closed parntheses is coming, if stack is empty incorrect case
# explanation say use recursion
# how to divide correct and incorrect part? i can' understand..
# 여는 괄호가 오면 +1 닫는 괄호가 오면 -1 따라서 값은 양수 또는 음수를 갖는다. 그러나 0되는 순간 이것은 균형잡힌 괄호이다.


# recursion
def solution(p):
    # base condition
    if not p:
        return ''

    flag = 0
    correct = False
    idx = 0
    if p[idx] == '(':
        flag += 1
        correct = True
    else:
        flag -= 1
    idx += 1

    while idx < len(p) and flag:
        if p[idx] == '(':
            flag += 1
        else:
            flag -= 1
        idx += 1
    # idx == len(p) 일때, flag는 무조건 0이다. Because input data is always balanced brackets string
    u = p[:idx]
    v = p[idx:]
    if correct:
        return u + solution(v)
    answer = '(' + solution(v) + ')'
    for bracket in u[1:idx - 1]:
        if bracket == '(':
            answer += ')'
        else:
            answer += '('
    return answer


if __name__=="__main__":
    p1 = "(()())()"
    p2 = ")("
    p3 = "()))((()"
    p4 = ")()()("
    print(solution(p1))  # "(()())()"
    print(solution(p2))  # "()"
    print(solution(p3))  # "()(())()"
    print(solution(p4))  # "()()()" X ((())) O
