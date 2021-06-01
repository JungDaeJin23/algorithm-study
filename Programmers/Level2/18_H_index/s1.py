# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
# 발표한 논문의 수는 1편 이상 1,000편 이하
# 논문별 인용 횟수는 0회 이상 10,000회 이하
# n = len(citations) 이때 h의 최댓값을 구하라
# condition 1. n개 중 len(citation >= h) >= h
# condtion 2. (All - (citation >= h)) <= h  ...? it's trivial


# recursion depth 넘어간다. while 로 하는 법..
def my_quick_sort(list1):
    if len(list1) <= 1:
        return list1
    left = []
    right = []
    pivot = 0
    for el in list1:
        if el < list1[pivot]:
            left.append(el)
        else:
            right.append(el)

    answer = my_quick_sort(left) + [list1[pivot]] + my_quick_sort(right)
    return answer


# 길이의 최댓값(논문 수)를 기준으로 그 값 이하부터 비교를 시작한다. 근데 정렬 후 비교 시작하면 그냥 해도 매한가지
def solution(citations):
    # citations = my_quick_sort(citations)
    citations.sort()
    for idx in range(len(citations)-1, -1, -1):
        # if len(citations) < citations[idx]:
        # h번 이상 인용된 논문 수 = len(citations) - idx, h = citations[idx]
        # 중복된 인용 수 있어도 상관 없음 별 차이 없음
        # h가 인용된 논문 수에 국한된 값이 아니다
        if len(citations) - idx >= citations[idx]:
            if idx == len(citations) - 1:
                return citations[idx]
            plus = 1
            while citations[idx] + plus <= citations[idx + 1] and len(citations) - idx - 1 >= citations[idx] + plus:
                plus += 1
            return citations[idx] + plus - 1
    answer = len(citations)
    return answer


if __name__ == "__main__":
    print(solution([7,7]))  # 2


# list 크기보다 K가 큼으로 counting은 좋지 않아 보인다.
# 다른 사람 코드 인용된 횟수와 역순 정렬 중 값이 역전되는 순간이 h가 최대가 되는 순간이다.
# c 8 7 4 3 2 1
# L 1 2 3 4 5 6
# h 1 2 3 3 2 1
# 문제를 풀때 그래프를 그려보는 습관을 드려보자.
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
if __name__ == "__main__":
    print(solution([7,7]))  # 2


# try it
def soltuion(citations):
    citations.sort(reverse=True)
    h_max = 0

    for cnt, h in enumerate(citations, start=1):
        if h_max < min(cnt, h):
            h_max = min(cnt, h)

    return h_max



