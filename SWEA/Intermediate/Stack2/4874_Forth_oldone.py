def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


# Forth
def forth(postfix_notation):
    operator_dict = {'+': add, '-': minus, '*': multiply, '/': divide}
    num_stack = [0] * len(postfix_notation)
    top = -1

    for item in postfix_notation:
        if item == '.':
            if top == 0:
                return num_stack[top]
            else:
                return "error"
        elif item in operator_dict.keys():
            # pop
            b = num_stack[top]
            top -= 1
            a = num_stack[top]
            top -= 1
            c = operator_dict.get(item)(a, b)
            # push
            top += 1
            num_stack[top] = c
        else:
            top += 1
            num_stack[top] = int(item)

    return None


# input and output
T = int(input())
for tc in range(1, T + 1):
    Expression = list(input().split())
    print("#{0} {1}".format(tc, forth(Expression)))
