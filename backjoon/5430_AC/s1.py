import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    commands = input().rstrip()
    size = int(input().rstrip())
    stack_string = input().rstrip()
    stack = []
    num = ''
    if size > 0:
        for idx in range(1, len(stack_string)):
            if stack_string[idx].isdigit():
                num += stack_string[idx]
            else:
                stack.append(num)
                num = ''
    front = 0
    rear = len(stack) - 1
    reverse = False
    for command in commands:
        if command == 'D':
            if front > rear:
                print("error")
                break
            if not reverse:
                front += 1
            else:
                rear -= 1
        else:
            reverse = not reverse
    else:
        ans = ''
        if not reverse:
            for idx in range(front, rear+1):
                ans += stack[idx]
                if idx != rear:
                    ans += ','
        else:
            for idx in range(rear, front-1, -1):
                ans += stack[idx]
                if idx != front:
                    ans += ','
        print('[' + ans + ']')
