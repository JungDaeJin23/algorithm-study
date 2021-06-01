# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 0, 1은 are not prime number
# brute force, permutation
# permutation nP1, nP2, ..., nPn
# exception condition: 1. 011 == 11 check first number is zero -> int and set
# 2. when elements are duplicated 11' == 1'1 -> set


# hint: nP1, nP2, ..., nPn 다 따로 하지말고 하는 중에 얻을 수 있다.
def get_all_perms(numbers, visited, a):
    global A

    for idx in range(len(numbers)):
        if not visited[idx]:
            visited[idx] = True
            A.append(get_all_perms(numbers, visited, a + numbers[idx]))
            visited[idx] = False
    return a

# numbers 최대 수까지 에라토스테네스의 체를 만들고 교집합을 구한다.
def prime_sieve(max_number):
    sieve = [True] * (max_number + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(max_number ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, max_number + 1, i):
                sieve[j] = False
    return sieve


def solution(numbers):
    global A
    visited = [False] * len(numbers)
    A = []
    get_all_perms(numbers, visited, '')
    possible_cases = set(map(int, A))
    # len(possible_cases), max(possible_cases) set도 지원한다.
    # for el in possible_cases: if el > max:, cnt++

    sieve_of_eratosthenes = prime_sieve(max(possible_cases))
    # prime_set = possible_cases & sieve_of_eratosthenes
    cnt = 0
    for case in possible_cases:
        if sieve_of_eratosthenes[case]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution("17"))  # 3
    print(solution("011"))  # 2
'''
테스트 5 〉	통과 (467.57ms, 36.6MB)
테스트 8 〉	통과 (815.64ms, 53.4MB)
'''
