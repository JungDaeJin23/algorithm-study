# bruteforce, permutation
# all cases have same digits so compare each digit number; Compare each digit because all cases have the same digit.
# ignore the first digit [have(x) being(o)] zero because zero is less than [every(x) all(o)] (digits) numbers
# 자릿수가 다르면 맨 앞만 비교하고 나머지는 뒤로 넘겨준다. X
# 자릿수가 다른면 짧은 쪽은 1의 자릿수가 계속 이어지게 비교한다. 456 vs 4 -> 44 => 456 > 4
# pruning if find smaller number
# recursion or while


# perm
def my_perm(numbers, used):
    a = ''
    index = 0
    while True:
        max_num = ''
        idx = int()
        for i in range(len(numbers)):
            # if not used[i]:
                if max_num:
                    if len(numbers[i]) > len(max_num):
                        repeat_time = len(numbers[i])
                        short = len(max_num)
                        s = 0
                        for j in range(repeat_time):
                            if int(max_num[s]) > int(numbers[i][j]):
                                break
                            elif int(max_num[s]) < int(numbers[i][j]):
                                max_num = numbers[i]
                                idx = i
                                break

                            if s + 1 < short:
                                s += 1
                    else:
                        repeat_time = len(max_num)
                        short = len(numbers[i])
                        s = 0
                        for j in range(repeat_time):
                            if int(max_num[j]) > int(numbers[i][s]):
                                break
                            elif int(max_num[j]) < int(numbers[i][s]):
                                max_num = numbers[i]
                                idx = i
                                break

                            if s + 1 < short:
                                s += 1

                else:
                    max_num = numbers[i]
                    idx = i

        if not max_num:
            break
        else:
            used[idx] = True
            # a += numbers[idx]
            # a = numbers[idx]
            a += numbers.pop(idx)
        # a += my_perm(numbers, used)
    return a


# selection sort
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        idx = i
        for j in range(i, len(numbers)):
            f = r = 0
            while True:
                if numbers[idx][f] > numbers[j][r]:
                    break
                elif numbers[idx][f] < numbers[j][r]:
                    idx = j
                    break

                if f == len(numbers[idx]) - 1 and r == len(numbers[j]) - 1:
                    break
                if f + 1 < len(numbers[idx]):
                    f += 1
                if r + 1 < len(numbers[j]):
                    r += 1

        numbers[idx], numbers[i] = numbers[i], numbers[idx]
    return numbers


# quick sort
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    left = []
    right = []
    pivot = 0
    for i in range(1, len(numbers)):
        if numbers[pivot] + numbers[i] > numbers[i] + numbers[pivot]:
            right.append(numbers[i])
        else:
            left.append(numbers[i])
        # f = r = 0
        # while True:
            # if numbers[pivot][f] > numbers[i][r]:
            #     right.append(numbers[i])
            #     break
            # elif numbers[pivot][f] < numbers[i][r]:
            #     left.append(numbers[i])
            #     break
            #
            # if f == len(numbers[pivot]) - 1 and r == len(numbers[i]) - 1:
            #     right.append(numbers[i])
            #     break
            # if f + 1 < len(numbers[pivot]):
            #     f += 1
            # if r + 1 < len(numbers[i]):
            #     r += 1
    answer = quick_sort(left) + [numbers[pivot]] + quick_sort(right)
    return answer


def solution(numbers):
    if not sum(numbers):
        return '0'
    numbers = list(map(str, numbers))
    used = [False] * len(numbers)
    # answer = my_perm(numbers, used)
    # answer = ''.join(selection_sort(numbers))
    answer = ''.join(quick_sort(numbers))
    return answer


if __name__ == "__main__":
    print(solution([6, 10, 2]))  # "6210
    print(solution([3, 30, 34, 5, 9]))  # 9534330
    print(solution([0, 0, 0]))
    print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 987654321101000
    print(solution([402212, 12]))  # 40221212
    print(solution([40, 404]))  # 40440
    print(solution([21, 212]))  #  출력 "21221"
    print(solution([40, 403]))  #
''' 
    [40, 405]
    [40, 404]
    [12, 121]
    [2, 22, 223]
    [21, 212]
    [41, 415]
    [2, 22]
    [70, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 1000]
    [12, 1213]
'''







####################################
# solved in the past, time over
def solution(numbers):
    numbers_str_list = list(map(str, numbers))
    for idx1 in range(len(numbers_str_list)):
        for idx2 in range(idx1 + 1, len(numbers_str_list)):
            if numbers_str_list[idx1][0] < numbers_str_list[idx2][0]:
                numbers_str_list[idx1], numbers_str_list[idx2] = numbers_str_list[idx2], numbers_str_list[idx1]
            elif numbers_str_list[idx1][0] == numbers_str_list[idx2][0]:
                len1 = len(numbers_str_list[idx1])
                len2 = len(numbers_str_list[idx2])
                for idx3 in range(len1) if len1 > len2 else range(len2):
                    if numbers_str_list[idx1][idx3 % len1] >= numbers_str_list[idx2][idx3 % len2]:
                        pass
                    else:
                        numbers_str_list[idx1], numbers_str_list[idx2] = numbers_str_list[idx2], numbers_str_list[idx1]
                        break
            else:
                pass

    answer = ''.join(numbers_str_list)
    return answer
