# binary search
def binary_search_cnt(total_pages, target_page):
    start = 1
    end = total_pages
    cnt = 0

    while start <= end:
        cnt += 1
        middle = int((start + end) / 2)
        if target_page == middle:
            break
        elif target_page < middle:
            # end = middle - 1
            end = middle
        else:
            # start = middle + 1
            start = middle
    return cnt


# recursion
def binary_search2(start, end, target_page):
    if start >= end:
        # return None
        return 1
    middle = int((start + end) / 2)
    if target_page == middle:
        return 1
    elif target_page < middle:
        return 1 + binary_search2(start, middle, target_page)
    else:
        return 1 + binary_search2(middle, end, target_page)

# input and output
T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    pa, pb = binary_search_cnt(P, Pa), binary_search_cnt(P, Pb)
    rpa, rpb = binary_search2(1, P, Pa), binary_search2(1, P, Pb)
    # if pa == pb:
    #     answer = 0
    # elif pa < pb:
    #     answer = 'A'
    # else:
    #     answer = 'B'
    if rpa ==rpb:
        answer = 0
    elif rpa < rpb:
        answer = 'A'
    else:
        answer = 'B'
    print("#{0} {1}".format(tc, answer))