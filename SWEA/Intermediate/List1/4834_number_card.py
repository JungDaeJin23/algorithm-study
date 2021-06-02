T = int(input())

for tc in range(1, T+1):
    # N은 C에서 String 일 경우 사이즈 필요해서 명시됨
    N = int(input())
    # 0 ≤ ai ≤ 9
    # counting list 활용 옛날거에서 아이디어 차용
    # arrary 1번만 순회해도 된다.
    ai = input()
    counting_list = [0]*10
    for num_str in ai:
        counting_list[int(num_str)] += 1
    idx = 0
    num_cnt = 0
    max_num = -1
    while idx < 10:
        # 갯수가 같으면 가장 큰 수로 출력한다. <= 등호로 같을 경우 갱신
        if num_cnt <= counting_list[idx]:
            num_cnt = counting_list[idx]
            max_num = idx
        idx += 1
    # 존재하는 가장 큰 수와 그것의 갯수가 아니라 가장 큰 수와 가장 많은 갯수이다.
    # idx = 9
    # while idx >= 0 and counting_list[idx] == 0:
    #     idx -= 1
    # max_num = idx
    # num_cnt = counting_list[idx]

    # arrary를 사용한 순회 검색
    # 리스트를 총 2번 순회
    # ai = list(map(int, input().split()))
    # max_num = 0
    # num_cnt = 0
    # for num in ai:
    #     if num > max_num:
    #         max_num = num
    #         num_cnt = 1
    #     elif num == max_num:
    #         num_cnt += 1

    print('#{0} {1} {2}'.format(tc, max_num, num_cnt))
