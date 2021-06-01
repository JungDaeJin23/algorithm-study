# greedy, counting sort
# greedy:
# the heavier person escapes first.
# if lighter one can get on a boat, escape together
def solution(people, limit):
    #     # counting sort. no just count
    #     weight_limitation: int = 240
    #     people_weight_status: list = [0] * (weight_limitation + 1)
    #     the_heaviest_weight: int = 40
    #     the_lightest_weight: int = weight_limitation
    #     for weight in people:
    #         people_weight_status[weight] += 1
    #         if weight > the_heaviest_weight:
    #             the_heaviest_weight = weight
    #         elif weight < the_lightest_weight:
    #             the_lightest_weight = weight

    #     # greedy
    #     answer = 0
    #     while the_heaviest_weight >= the_lightest_weight:
    #         while people_weight_status[the_heaviest_weight]:
    #             people_weight_status[the_heaviest_weight] -= 1
    #             if the_heaviest_weight + the_lightest_weight <=limit:
    #                 people_weight_status[the_lightest_weight] -= 1
    #                 while not people_weight_status[the_lightest_weight]:
    #                     the_lightest_weight += 1
    #         while not people_weight_status[the_heaviest_weight]:
    #             the_heaviest_weight -= 1
    # 그냥 정렬하는게 더 편함 counting_sort
    weight_limitation: int = 240
    people_weight_status: list = [0] * (weight_limitation + 1)
    for weight in people:
        people_weight_status[weight] += 1
    # 누적 accumulate the count
    people_weight_accumulative_status: list = people_weight_status[:]
    for i in range(1, len(people_weight_accumulative_status)):
        people_weight_accumulative_status[i] += people_weight_accumulative_status[i - 1]
    sorted_people = people[:]
    for weight in people:
        sorted_people[people_weight_accumulative_status[weight] - 1] = weight
        people_weight_accumulative_status[weight] -= 1

    # greedy
    # 무거운 사람 먼저 나간다. 이때 가벼운 사람이 같이 탈 수 있으면 같이 태움
    # 리스트 뒤에서 한 사람 태우고 앞에서부터 가능한 한 많이 태운다.
    answer = 0
    # 그냥 큐로 하자. 뒤에서 한명 앞에서 가능한 한 많이
    rear = len(people) - 1
    front = -1
    while front != rear:  # is_empty
        boat = 0
        # 뒤에서 한명
        boat += sorted_people[rear]
        rear -= 1
        # 앞에서 가능한 많이 사람이 빌 때까지
        while front != rear:
            # 탈 수 없다면 break
            if boat + sorted_people[front + 1] > limit:
                break
            front += 1
            boat += sorted_people[front]
        # 보트가 한 번 나갔으므로 횟수 세어준다.
        answer += 1
    # cnt_person = len(people)
    # cnt_escaped_person = 0
    # heaviest_idx = len(people) - 1
    # lightest_idx = 0
    # # while cnt_escaped_person < cnt_person:
    # while lightest_idx < heaviest_idx:
    #     boat = 0
    #     # 못타는 경우 없음 여기서는 사람 없는지 확인 안해도 됨 위에서 카운트로 걸러짐
    #     boat += sorted_people[heaviest_idx]
    #     # 무거운 사람 한명 태움
    #     cnt_escaped_person += 1
    #     # 여기서는 탄 사람 표시 해줄 필요 없음 X 필요 있음
    #     # 필요 없음 인덱스로 확인하면 됨
    #     # sorted_people[heaviest_idx] = 0
    #     heavest_idx -= 1
    #     while boat + sorted_people[lightest_idx] <= limit:
    #         boat += sorted_people[lightest_idx]
    #         cnt_escaped_person += 1
    #         lightest_idx += 1
    #         # 자리는 남았지만 더는 사람이 없을 경우
    #         if ligtest_idx
    #     answer += 1

    return answer