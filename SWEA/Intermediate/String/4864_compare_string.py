# 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    boundary_condition = len(str2) - len(str1)
    found = False
    idx = 0
    # 5 - 3 = 2 이므로 = 등호 포함해줘야 된다.
    while idx <= boundary_condition:  # and not found:
        str1_idx = 0
        # old one 과 비교해서 반복 횟수는 동일 차이점은 인덱스를 1씩 더해주다가 빼줘서 틀린지점으로 회귀하거나 ~~
        while str1_idx < len(str1):
            if str1[str1_idx] != str2[idx + str1_idx]:
                break
            str1_idx += 1
        else:
            found = True
            break
        idx += 1

    print('#{0} {1}'.format(tc, int(found)))
