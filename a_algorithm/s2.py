from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    subways = list(map(int, input().split()))
    comb = combinations([i for i in range(N)], 4)
    answer = 0
    for a, b, c, d in comb:
        # 두 역을 연결하는 직통 노선 and 직통 노선 간의 인접 확인
        if b - a == 1 or c - b == 1 or d - c == 1 or d - a == N - 1:
            continue
        # 교차 확인

        tmp = (subways[a] + subways[b]) ** 2 + (subways[c] + subways[d]) ** 2
        if tmp > answer:
            answer = tmp
        tmp = (subways[b] + subways[c]) ** 2 + (subways[d]+ subways[a]) ** 2
        if tmp > answer:
            answer = tmp
    print('#{0} {1}'.format(tc, answer))