# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬
T = int(input())
# counting sort를 이용한 방법도 있다. 최댓값 100
# 특별히 정렬된 숫자를 10개까지 출력한다.

for tc in range(1, T+1):
    N = input()
    arr = list(map(int, input().split()))
    arr.sort()
    sol_arr = [0] * 10

    idx = 0
    acs_idx = 0
    des_idx = len(arr) - 1
    while idx < 10:
        if idx % 2:
            tmp = arr[acs_idx]
            acs_idx += 1
        else:
            tmp = arr[des_idx]
            des_idx -= 1
        sol_arr[idx] = tmp
        idx += 1

    print("#{0}".format(tc), *sol_arr)
    # print('#{0}'.format(tc), end=' ')
    # print(*sol_arr)
