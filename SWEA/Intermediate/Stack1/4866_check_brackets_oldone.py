def check_matching(data):
    stack = []
    # ASCII code ( = 40, ) = 41,[ = 91, ] = 93, 123 = {, 125 = }
    bra = ['[', '{', '(']
    ket = [']', '}', ')']
    for d in data:
        if d in bra:
            stack.append(d)
        elif d in ket:
            checker = ord(d) - 1 if ord(d) == 41 else ord(d) - 2
            # there is no case when stack is empty, pop execute
            if len(stack) == 0:
                return 0
            elif ord(stack.pop()) != checker:
                return 0
    if len(stack) == 0:
        return 1
    return 0


# input and output
T = int(input())
for tc in range(1, T + 1):
    Str1 = input()
    print("#{0} {1}".format(tc, check_matching(Str1)))
