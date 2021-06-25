import sys


M = int(input())
S = set()
# ans = ''
for _ in range(M):
    command = sys.stdin.readline().split()
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if command[0] == 'add':
        S.add(int(command[1]))
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif command[0] == 'remove':
        tmp = int(command[1])
        if tmp in S:
            S.remove(tmp)
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif command[0] == 'check':
        print(int(int(command[1]) in S))
        # ans += '1\n' if el in S else '0\n'
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif command[0] == 'toggle':
        tmp = int(command[1])
        if tmp in S:
            S.remove(tmp)
        else:
            S.add(tmp)
    elif command[0] == 'all':
        S = set(range(1, 21))
    # elif command[0] == 'empty':
    else:
        # empty: S를 공집합으로 바꾼다.
        S = set()
