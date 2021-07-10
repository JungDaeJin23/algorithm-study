# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = [0] * 10000
top = -1


def pop():
    global top, stack
    if top > -1:
        print(stack[top])
        top -= 1
    else:
        print(-1)


def size():
    global top
    print(top + 1)


def empty():
    global top
    if top > -1:
        print(0)
    else:
        print(1)


def stack_top():
    global top, stack
    if top > -1:
        print(stack[top])
    else:
        print(-1)


order_dict = {'pop': pop, 'size': size, 'empty': empty, 'top': stack_top}
for _ in range(N):
    order = input().rstrip()
    if order_dict.get(order):
        order_dict[order]()
    else:
        order, num = order.split()
        top += 1
        stack[top] = num