# brute force
def word_counter(str1, str2):
    max_cnt = 0
    for alphabet1 in str1:
        cnt = 0
        for alphabet2 in str2:
            if alphabet1 == alphabet2:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt


# input and output
T = int(input())
for tc in range(1, T + 1):
    Str1, Str2 = input(), input()
    print("#{0} {1}".format(tc, word_counter(Str1, Str2)))