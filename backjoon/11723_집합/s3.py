import sys
M = int(input())
S = 0
# ans = ''
for _ in range(M):
    command = sys.stdin.readline().split()
    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if command[0] == 'add':
        S |= 1 << int(command[1])
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif command[0] == 'remove':
        tmp = 1 << int(command[1])
        if S & tmp:
            S -= tmp
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif command[0] == 'check':
        print(1 if S & 1 << int(command[1]) else 0)
        # ans += '1\n' if S & 1 << el else '0\n'
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif command[0] == 'toggle':
        S ^= 1 << int(command[1])
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    elif command[0] == 'all':
        S = 0b11111111111111111111
    # elif command == 'empty':
    else:
        # empty: S를 공집합으로 바꾼다.
        S = 0
# print(ans)
