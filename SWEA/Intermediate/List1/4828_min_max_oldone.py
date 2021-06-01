
# input
T = int(input())
size_list = list()
num_list = list()
for tc in range(1, T+1):
    size_list.append(int(input()))
    num_list.append(list(map(int, input().split())))


def diff_min_max(numbers_list):
    min_val = numbers_list[0]
    max_val = numbers_list[0]

    for num in numbers_list:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return max_val - min_val


# output
for tc in range(1, T+1):
    print("#{0} {1}".format(tc, diff_min_max(num_list[tc-1])))
