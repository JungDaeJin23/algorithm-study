T = int(input())


def binary_search(l, r, target, cnt=1):
    c = int((l+r)/2)
    if c == target:
        return cnt

    if target < c:
        return binary_search(l, c, target, cnt=cnt+1)
    else:
        return binary_search(c, r, target, cnt=cnt+1)


for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_a = binary_search(1, P, Pa)
    cnt_b = binary_search(1, P, Pb)

    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_b < cnt_a:
        winner = 'B'
    else:
        winner = 0
    print('#{0} {1}'.format(tc, winner))
