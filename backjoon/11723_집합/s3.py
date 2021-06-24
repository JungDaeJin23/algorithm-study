M = int(input())
S = 0

for _ in range(M):
    command = input()
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    if command == 'all':
        S = 0b11111111111111111111
    elif command == 'empty':
        # empty: S를 공집합으로 바꾼다.
        S = 0
    else:
        operator, el = command.split()
        el = int(el)
        # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
        if operator == 'add':
            S |= 1 << el
        # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
        elif operator == 'remove':
            tmp = 1 << el
            if S & tmp:
                S -= tmp
        # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
        elif operator == 'check':
            print(1 if S & 1 << el else 0)
        # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
        else:
            S ^= 1 << el

