# 개발언어 항목에 cpp, java, python
# 지원 직군 항목에 backend와 frontend
# 지원 경력구분 항목에 junior와 senior
# 선호하는 소울푸드로 chicken과 pizza
# 점수 몇점 이상


# global로 공유해도 좋을 것 같다.
# Language, job, carrer, food 하나로 작업 가능
def condition(info_list, people, query, idx):
    for i, info in enumerate(info_list):
        if query.isdigit():
            if int(info[idx]) >= int(query):
                pass
            else:
                people[i] = False
        else:
            if info[idx] == query:
                pass
            else:
                people[i] = False

    return people


# Brute force
def solution(info, query):
    info_list = [list(info[idx].split()) for idx in range(len(info))]
    query_list = [list(query[idx].split()) for idx in range(len(query))]
    answer = [0] * len(query)
    # idx        0         2          4      6     7
    # condition  language  category   career food  score
    # condition = {0: condition0, 1: condition1, 2: condition2, 3: condition3}

    for i, q in enumerate(query_list):
        people = [True] * len(info)
        for idx in range(0, len(q), 2):

            if q[idx] == '-':
                pass
            else:
                people = condition(info_list, people, q[idx], idx//2)
        people = condition(info_list, people, q[len(q) - 1], len(info_list[0]) - 1)
        answer[i] = sum(people)
    return answer


if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
    # [1, 1, 1, 1, 2, 4]

# pruning
def solution(info, query):
    info_list = [list(info[idx].split()) for idx in range(len(info))]
    # hyphen 과 조건으로만 query  구성하자
    query_list = [[el for el in query[idx].split() if el != 'and'] for idx in range(len(query))]
    answer = [0] * len(query)

    for idx, queries in enumerate(query_list):
        cnt = 0
        for person in info_list:
            for j, query in enumerate(queries):
                if query == '-':
                    pass
                else:
                    if query.isdigit():
                        if int(person[j]) < int(query):
                            break
                    else:
                        if person[j] != query:
                            break
            else:
                cnt += 1
        answer[idx] = cnt

    return answer


if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
    # [1, 1, 1, 1, 2, 4]


def make_key(queries):
    key_list = ['']
    # language = ['cpp', 'java', 'python']
    # job = ['backend', 'frontend']
    # career = ['junior', 'senior']
    # food = ['chicken', 'pizza']
    category = [['cpp', 'java', 'python'], ['backend', 'frontend'], ['junior', 'senior'], ['chicken', 'pizza']]
    for idx, query in enumerate(queries):
        if query == '-':
            for j in range(len(key_list)):
                for new in category[idx]:
                    key_list[j] += new
        else:
            for j in range(len(key_list)):
                key_list[j] += query

# memoization, 마지막 점수는 1 ~ 5000 원소를 세는 것이 좋겠다.
# 그외에는 다 분류를 하자 3 * 2 * 2 * 2 종류에 점수를 집어넣자 O(n + k)
# 키 만들지 말고 - 까지 넣어서 4 * 3 * 3 * 3 ?
# 어느 인덱스에 할당해 줄까? dict?
def solution(info, query):

    classification = {}
    info_list = [list(info[idx].split()) for idx in range(len(info))]
    for person in info_list:
        key = ''
        for idx in range(len(person) - 1):
            key += person[idx]
        if classification.get(key):
            classification[key].append(person[idx + 1])
        else:
            classification[key] = [person[idx + 1]]
    # hyphen 과 조건으로만 query  구성하자
    query_list = [[el for el in query[idx].split() if el != 'and'] for idx in range(len(query))]
    answer = [0] * len(query)

    for idx, queries in enumerate(query_list):
        cnt = 0

        answer[idx] = cnt

    return answer

if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
    # [1, 1, 1, 1, 2, 4]

def search_bin_tree(bin_tree, queries, classification, idx=0, target=0):
    cnt = 0
    if idx == len(queries) - 1:
        for score in bin_tree[target]:
            # type 확인 잘하자!
            if int(score) >= int(queries[idx]):
                cnt += 1
        return cnt

    if queries[idx] == '-':
        for key, course in classification[idx].items():
            cnt += search_bin_tree(bin_tree, queries, classification, idx + 1, 2 * target + course)
    else:
        target += classification[idx].get(queries[idx]) + target
        cnt += search_bin_tree(bin_tree, queries, classification, idx + 1, target)

    return cnt
#
def solution(info, query):
    language = {'cpp': 0, 'java': 1, 'python': 2}
    job = {'backend': 0, 'frontend': 1}
    career = {'junior': 0, 'senior': 1}
    food = {'chicken': 0, 'pizza': 1}
    classification = [language, job, career, food]
    bin_tree = [[] for _ in range(len(language) * len(job) * len(career) * len(food))]
    info_list = [list(info[idx].split()) for idx in range(len(info))]
    for person in info_list:
        idx = 0
        for i in range(len(person) - 1):
            idx += classification[i].get(person[i]) + idx
        bin_tree[idx].append(person[len(person) - 1])
    # print(bin_tree)
    # hyphen 과 조건으로만 query  구성하자
    query_list = [[el for el in query[idx].split() if el != 'and'] for idx in range(len(query))]
    answer = [0] * len(query)

    for idx, queries in enumerate(query_list):
        cnt = search_bin_tree(bin_tree, queries, classification)
        answer[idx] = cnt

    return answer

if __name__ == "__main__":
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
    # [1, 1, 1, 1, 2, 4]
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["- and - and - and - 150"]))


# search binary tree
def search_bin_tree(bin_tree, queries, classification, idx=0, target=0):
    cnt = 0
    if idx == len(queries) - 1:
        for ii, score in enumerate(bin_tree[target]):
            # type 확인 잘하자!
            # 여기서 속도가 오래 걸릴수도.. 동윤님 코드 참조
            if int(score) >= int(queries[idx]):
                cnt = len(bin_tree[target]) - ii
                break
        return cnt
        #         cnt += 1
        # return cnt

    if queries[idx] == '-':
        for key, course in classification[idx].items():
            cnt += search_bin_tree(bin_tree, queries, classification, idx + 1, 2 * target + course)
    else:
        target += classification[idx].get(queries[idx]) + target
        cnt += search_bin_tree(bin_tree, queries, classification, idx + 1, target)

    return cnt


def solution(info, query):
    language = {'cpp': 0, 'java': 1, 'python': 2}
    job = {'backend': 0, 'frontend': 1}
    career = {'junior': 0, 'senior': 1}
    food = {'chicken': 0, 'pizza': 1}
    classification = [language, job, career, food]
    # language = [[], [], []]
    # job = [[], []]
    # career = [[], []]
    # food = [[], []]
    bin_tree = [[] for _ in range(len(language) * len(job) * len(career) * len(food))]
    # B = {'cpp': 0, 'java': 1, 'python': 2, 'backend': 0, 'frontend': 1, 'junior': 0, 'senior': 1, 'chicken': 0, 'pizza': 1}
    info_list = [list(info[idx].split()) for idx in range(len(info))]
    # print(info_list)
    for person in info_list:
        idx = 0
        for i in range(len(person) - 1):
            idx += classification[i].get(person[i]) + idx
        bin_tree[idx].append(person[len(person) - 1])
    for ii in range(len(bin_tree)):
        bin_tree[ii].sort()
    # print(bin_tree)
    # hyphen 과 조건으로만 query  구성하자
    query_list = [[el for el in query[idx].split() if el != 'and'] for idx in range(len(query))]
    # print(query_list)
    answer = [0] * len(query)

    for idx, queries in enumerate(query_list):
        cnt = search_bin_tree(bin_tree, queries, classification)
        answer[idx] = cnt

    return answer


if __name__ == "__main__":
    # import time
    # start_time = time.time()
    # a = [[] for _ in range(16)]
    # for i in range(16):
    #     for j in range(500000):
    #         a[i].append(j)
    # print(time.time() - start_time)  # 4.385967254638672
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
    # [1, 1, 1, 1, 2, 4]
    print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["- and - and - and - 150"]))
