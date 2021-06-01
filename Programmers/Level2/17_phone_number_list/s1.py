# brute force 단순 비교는 경우가 많고 비교하기 복잡할 것으로 예상된다.


# hash?
def solution(phone_book):
    answer = True
    phone_book_dictionary = dict(zip(phone_book, [1 for _ in range(len(phone_book))]))
    for phone in phone_book:
        key = ''
        for num in phone:
            key += num
            if phone_book_dictionary.get(key):
                if phone_book_dictionary[key] >= 2:
                    return False
                phone_book_dictionary[key] += 1

    return answer


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
'''
테스트 3 〉	통과 (626.14ms, 48.2MB)
테스트 4 〉	통과 (239.04ms, 35.9MB)
'''


# try it without a dictionary type
# 길이순 정렬 sort in length order, 앞에서부터 순차적으로 비교 O(n^2)
def solution(phone_book):
    answer = True
    return answer


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))


# try it without a dictionary type
# 모든 원소들의 앞자리를 가져온다. 일치하는 것만 남기고 계속 가져온다.
# 한 원소의 길이가 끝났을 때 남아있는 같은 인덱스에 원소가 2개 이상이면 False O(n)
# 각 전화번호의 길이는 1 이상 20 이하, phone_book의 길이는 1 이상 1,000,000 이하 => 20 * 1,000,000
# dfs? back tracking?
def is_promising(phone_book, promising, phone_idx):
    # cnt = 0
    for idx_list in promising:
        if len(idx_list) >= 2:
            new_promising = [[] for _ in range(10)]
            # cnt += 1
            for idx in idx_list:
                if len(phone_book[idx]) == phone_idx:
                    return False
                new_promising[int(phone_book[idx][phone_idx])].append(idx)
            if not is_promising(phone_book, new_promising, phone_idx + 1):
                return False
    # escape condition: 중복되는 것이 하나도 없었으며, (그때 끝나는 값도 없었다.) <- 필요한 조건은아니다.
    # 위의 두 조건을 제외하고는 전부 참이다.
    # if not cnt:
    #     return True
    # 왜 트루이지? 223 226 =>
    return True


def solution(phone_book):
    answer = True
    promising = [[] for _ in range(10)]  # 0 ~ 9
    phone_idx = 0
    for idx in range(len(phone_book)):
        promising[int(phone_book[idx][phone_idx])].append(idx)

    if is_promising(phone_book, promising, phone_idx + 1):
        return True
    return False


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))

'''
테스트 3 〉	통과 (1084.46ms, 57.3MB)
테스트 4 〉	통과 (270.90ms, 32.1MB)
'''
