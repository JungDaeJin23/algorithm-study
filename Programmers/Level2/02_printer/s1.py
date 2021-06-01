# priority counting list and circular queue


# counting sort
def counting_sort(priorities):
    highest_priority = 9
    count = [0] * (highest_priority + 1)
    for priority in priorities:
        count[priority] += 1

    # stable sort 하고 싶으면 누적을 해야 된다.
    for i in range(len(count) - 1):
        count[i + 1] += count[i]
    # 내림차순
    # total = 0
    # for i in range(len(count) - 1, -1, -1):
    #     count[i], total = count[i] + total, count[i] + total

    sorted_priorities = priorities[:]
    for element in priorities:
        sorted_priorities[count[element] - 1] = element
        count[element] -= 1

    return sorted_priorities
# print(counting_sort([4,3,6,3,1]))


def solution(priorities, location):
    # printed_cnt = 0
    sorted_priorities_stack = counting_sort(priorities)
    top = len(sorted_priorities_stack) - 1

    circular_queue = [0] + priorities
    n = len(circular_queue)
    front = 0
    rear = n - 1

    while top != -1:
        if sorted_priorities_stack[top] == circular_queue[(front + 1) % n]:
            if location == 0:
                return len(priorities) - top
            # printed_cnt += 1
            front = (front + 1) % n
            top -= 1
            # if location == 0:
            #     return printed_cnt
            location -= 1
        else:
            # dequeue
            front = (front + 1) % n
            document_priority = circular_queue[front]
            # enqueue
            rear = (rear + 1) % n
            circular_queue[rear] = document_priority
            location -= 1

        if location == -1:
            # 프린트가 되면 대기중인 숫자가 줄어드는데 생각없이 len(priorites)로 했음
            location += top + 1
    return None


##################################################
# 옛날에 짠거
# def max_from_str_n_int_mixed_list(str_n_int_mixed_list):
#     max_val = int(str_n_int_mixed_list[0])
#     for val in str_n_int_mixed_list:
#         if (val if isinstance(val, int) else int(val)) >= max_val:
#             max_val = val if isinstance(val, int) else int(val)
#     return max_val
#
#
# def solution(priorities, location):
#     stack_stage = []
#     priorities[location] = str(priorities[location])
#     while len(priorities) != 1:
#         check_stage_num = priorities.pop(0)
#
#         if int(check_stage_num) >= max_from_str_n_int_mixed_list(priorities):
#             print(max_from_str_n_int_mixed_list(priorities))
#             stack_stage.append(check_stage_num)
#
#         else:
#             priorities.append(check_stage_num)
#
#     stack_stage.append(priorities.pop(0))
#
#     for idx, val in enumerate(stack_stage):
#         if isinstance(val, str):
#             answer = idx + 1
#             break
#     return answer


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))  # 1
    print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
    print(solution([2,2,2,1,3,4], 3))
