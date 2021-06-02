
def card_checker(num_str):
    num_info_list = [0] * 10
    for num in num_str:
        num_info_list[int(num)] += 1

    max_num = 0
    max_cnt = 0
    for num, cnt in enumerate(num_info_list):
        if cnt >= max_cnt:
            max_num = num
            max_cnt = cnt
    return max_num, max_cnt


# input and output
T = int(input())
for tc in range(1, T+1):
    size_num_str = input()
    number_str = input()
    result = card_checker(number_str)
    print("#{0} {1} {2}".format(tc, result[0], result[1]))
