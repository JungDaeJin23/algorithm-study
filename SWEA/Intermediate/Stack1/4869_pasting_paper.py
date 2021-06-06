T = int(input())
# 10: 1, 20: 3, 30: 5, 40: 5 + 3*2 == 11, 50: 11 + 5*2 == 21
# x(n-2)*2 + x(n-1) = x(n)
# memoization
cases_of_pattern = [0, 1, 3]
for tc in range(1, T+1):
    N = int(input())
    target_idx = N // 10
    while target_idx >= len(cases_of_pattern):
        tmp = cases_of_pattern[len(cases_of_pattern)-2]*2 + cases_of_pattern[len(cases_of_pattern)-1]
        cases_of_pattern.append(tmp)

    print('#{0} {1}'.format(tc, cases_of_pattern[target_idx]))
