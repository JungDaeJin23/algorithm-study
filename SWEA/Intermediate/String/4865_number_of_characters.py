# 두 개의 문자열 str1과 str2가 주어진다.
# 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_set = set(str1)
    str1_key_dict = dict.fromkeys(str1_set, 0)
    for character in str2:
        if str1_key_dict.get(character, -1) != -1:
            str1_key_dict[character] += 1
    # max_cnt = sorted(str1_key_dict.items(), key=lambda x: x[1], reverse=True)[0][1]
    max_cnt = sorted(str1_key_dict.values(), reverse=True)[0]
    # max_cnt = 0
    # for cnt in str1_key_dict.values():
    #     if max_cnt < cnt:
    #         max_cnt = cnt
    print('#{0} {1}'.format(tc, max_cnt))
