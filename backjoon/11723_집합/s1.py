import sys
M = int(input())
set_arr = [0]*21
# ans = ''
for _ in range(M):
    command = sys.stdin.readline().split()
    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if command[0] == 'add':
        set_arr[int(command[1])] = 1
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif command[0] == 'remove':
        set_arr[int(command[1])] = 0
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif command[0] == 'check':
        print(set_arr[int(command[1])])
        # ans += str(set_arr[int(command[1]]) + '\n'
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif command[0] == 'toggle':
        num = int(command[1])
        set_arr[num] = 0 if set_arr[num] else 1
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    elif command[0] == 'all':
        set_arr = [1]*21
        # for i in range(1, 21):
        #     set_arr[i] = 1
    # elif command == 'empty':
    else:
        # empty: S를 공집합으로 바꾼다.
        set_arr = [0]*21
        # for i in range(1, 21):
        #     set_arr[i] = 0
# print(ans)