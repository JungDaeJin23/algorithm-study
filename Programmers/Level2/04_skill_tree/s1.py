# follow the sequence 순서를 지켜야 된다 -> 스택?
# make token 스택에 쌓아서 꺼내고 연삭식 처럼 일일히 비교할 필요 없음
# 스킬트리를 바로 스택으로 만들고 해당하는 요소가 들어왔을 때 top 위치만 보고 판단하면됨, 중복해서 주어지지 않으므로


def solution(skill, skill_trees):
    # prior_skill_order = dict(zip(skill, range(len(skill))))
    prior_skill_order_stack = list(skill)
    top = -1
    cnt = 0

    for skill_tree in skill_trees:
        top = -1
        for alphabet in skill_tree:
            if alphabet in skill:
                top += 1
                if prior_skill_order_stack[top] != alphabet:
                    break
        else:
            cnt += 1
    return cnt


##################
# solved in the past
# def solution(skill, skill_trees):
#     answer = 0
#     origin_skill = skill
#     for skill_tree_str in skill_trees:
#         skill = origin_skill
#         check = True
#         for val in skill_tree_str:
#             if val in skill and val == skill[0]:
#                 skill = skill[1:]
#                 check = True
#             elif val in skill and val != skill[0]:
#                 check = False
#                 break
#             else:
#                 pass
#         if check:
#             answer += 1
#     return answer


if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
