# Again(once more) too long explanation
# compose(x) organize the set menu. the set menus consist of popular single products.\
# at least twice ordered recipe can be in
# sort alphabet in ascending order
# 횟수? counting list?
# brute force는 부분집합 개념 차용해서 모든 조합을 기록한다. record? count all combinations
# 그래프? 양방향 엣지를 가진. 이것도 완전 탐색


# compare alphabets priority
# str1[len(str1):] = ''
def is_less_than(str1, str2):
    if not str1:
        return True
    if not str2:
        return False
    if ord(str1[0]) < ord(str2[0]):
        return True
    elif ord(str1[0]) > ord(str2[0]):
        return False
    else:
        # while 로 index 접근도 가능
        return is_less_than(str1[1:], str2[1:])


# sort in dictionary order
def alphabet_sort(iterables):
    for i in range(len(iterables) - 1):
        for idx in range(len(iterables) - 1 - i):
            if not is_less_than(iterables[idx], iterables[idx + 1]):
                iterables[idx], iterables[idx + 1] = iterables[idx + 1], iterables[idx]

    return iterables


if __name__ == "__main__":
    A1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    print(alphabet_sort(A1))


# dictionary + combination key
def comb(iterables, k, d=0, i=0):
    global visited, keys
    if d >= k:
        key = ''
        for idx, checker in enumerate(visited):
            if checker:
                key += iterables[idx]
        keys.append(''.join(sorted(list(key))))
        return
    # i = 0
    while i < len(iterables):
        if not visited[i]:
            visited[i] = True
            comb(iterables, k, d + 1, i)
            visited[i] = False
        i += 1


def solution(orders, course):
    global visited, keys
    result = []
    for course_length in course:
        cases_of_combination = {}
        for order in orders:
            if len(order) >= course_length:
                keys = []
                visited = [False] * len(order)
                comb(order, course_length)
                for key in keys:
                    if cases_of_combination.get(key):
                        cases_of_combination[key] += 1
                    else:
                        cases_of_combination[key] = 1
        max_count = 0
        for key, count in cases_of_combination.items():
            if count > max_count:
                max_count = count
        for key, count in cases_of_combination.items():
            if count > 1 and count == max_count:
                result.append(key)
    result.sort()
    return result


if __name__=="__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

"""
테스트 13 〉	통과 (10.61ms, 10.4MB)
테스트 14 〉	통과 (12.44ms, 10.3MB)
테스트 15 〉	통과 (11.31ms, 10.3MB)
테스트 16 〉	통과 (4.92ms, 10.2MB)
테스트 17 〉	통과 (9.97ms, 10.3MB)
테스트 18 〉	통과 (10.27ms, 10.3MB)
테스트 19 〉	통과 (3.18ms, 10.3MB)
테스트 20 〉	통과 (12.37ms, 10.2MB)
"""
############################


# graph, adjacency matrix 이것도 결국 조합이다.
def solution(orders, course):
    adjacency_matrix = [[0] * 26 for _ in range(26)]
    max_row = max_col = 0
    for order in orders:
        for i in range(len(order)):
            row = ord(order[i]) - ord('A')
            for j in range(i, len(order)):
                col = ord(order[j]) - ord('A')
                adjacency_matrix[row][col] += 1
                if adjacency_matrix[row][col] > adjacency_matrix[max_row][max_col]:
                    max_row = row
                    max_col = col
    for volume in course:
        pass


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
##########################
# I give it up!
# 카운팅 리스트로 각 메뉴끼리 비교해도 구분은 가능하다... 장점 문자열이 역으로 적혀있는 것도 별도의 가공이 필요 없다. XW == WX
# ABCDE, ACD
# A C D 에서 2임으로 2가 3개있으므로 3개인 조합에 추가 근데 이걸 완전 탐색 해줘야 됨..
# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열
# course 배열의 크기는 1 이상 10 이하
# 최대 경우의수 course 1 ~ 10, len(orders) = 20, orders 요소의 갯수(문자열 길이) 전부 10
# 카운트는 최초 1회만 진행하고 저장? couting_list = [0] * 26
# 1: 1~19까지합 210 * 횟수 10 == 2100
# 조합을 각 길이에 맞게 구하는 것은?
# (10C1 ~ 10C10) * 20 = (1024 - 1) * 20 파스칼의 삼가형 각 행의 합은 해당 2의 행 번째 재곱이다. == 20480
# 더 적네?
# 그냥 비교만 해주면 나오는 값은 무조건 2개이상 메뉴에서 나오므로 따로 검사안해줘도 되고 나오는 값이 바로 해당 길이의 코스가 된다.


def solution(orders, course):
    orders_counting_lists = [[0]*26 for _ in range(len(orders))]
    for idx, order in enumerate(orders):
        for alphabet in order:
            orders_counting_lists[idx][ord(alphabet) - ord('A')] += 1
    possible_course = [[] for _ in range(11)]
    # 전부 비교 O(n^2*k)이네..
    for str1_idx in range(len(orders)):
        A = [0] * 26
        for str2_idx in range(str1_idx + 1, len(orders)):
            for idx in range(26):
                A[idx] = orders_counting_lists[str1_idx][idx] + orders_counting_lists[str2_idx][idx]
            cnt = 0
            a = ''
            # 가능한 경우 중  가장 긴것만 봐도 안되는 거네..
            for idx in range(len(A)):
                if A[idx] == 2:
                    cnt += 1
                    a += chr(idx + ord('A'))
            if cnt:
                possible_course[cnt].append(a)
    # 가능한 경우에서도 제일 많은 경우들만 남겨야 되네..
    # 결국 여기서도 가장 긴 것의 하위 조합들을 봐야되는 구나..
    answer = []
    for course_length in course:
        for menu in possible_course[course_length]:
            if menu not in answer:
                answer.append(menu)
    print(possible_course)
    return sorted(answer)


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
