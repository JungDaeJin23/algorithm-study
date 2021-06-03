# special_sort using selecting sort and delta direction(== switch)
def special_sort(l):
    # Variable name find_max instead of converter is also good
    converter = True
    list_length = len(l)

    i = 0
    while i < list_length:
        cmp_idx = i

        j = i
        while j < list_length:
            if converter and l[j] > l[cmp_idx]:
                cmp_idx = j
            elif (not converter) and l[j] < l[cmp_idx]:
                cmp_idx = j
            j += 1

        l[i], l[cmp_idx] = l[cmp_idx], l[i]
        converter = not converter
        i += 1

    return l[:10]


# input and output
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    print("#{0}".format(tc), *special_sort(L))