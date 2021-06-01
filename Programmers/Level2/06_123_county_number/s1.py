# permutation with repetition 중복 순열


def permutation(iterables):
    # wrong!!
    initial_state = iterables[:]
    visited = [False] * len(iterables)
    cnt = 0
    for i in range(len(iterables) - 1):
        cnt += 1
        print(iterables, cnt)
        iterables[i], iterables[i + 1] = iterables[i + 1], iterables[i]

    while iterables != initial_state:
        for i in range(len(iterables) - 1):
            cnt += 1
            print(iterables, cnt)
            iterables[i], iterables[i + 1] = iterables[i + 1], iterables[i]


def perm(iterables):
    global visited, A, cnt
    for i in range(len(iterables)):
        if not visited[i]:
            visited[i] = True
            A.append(iterables[i])
            perm(iterables)
            visited[i] = False
            A.pop(-1)
    if len(A) == 4:
        cnt += 1
        print(A, cnt)


def permutation_with_repetition(iterables, k, n):
    global answer, A, cnt, top
    if answer:
        return
    if top == k - 1:
        cnt += 1
        if cnt == n:
            # print(A, cnt)
            answer = A[:]
        return
    # if len(A) < k:
    if top < k:
        for i in range(len(iterables)):
            # A.append(iterables[i])
            top += 1
            A[top] = iterables[i]
            permutation_with_repetition(iterables, k, n)
            top -= 1
            # A.pop(-1)
    # if len(A) == k:
    # if top == k - 1:
    #     cnt += 1
    #     if cnt == n:
    #         # print(A, cnt)
    #         answer = A[:]


def solution(n):
    global answer, A, cnt, top
    answer = []
    A = []
    top = -1
    cnt = 0
    country_number = [1, 2, 4]
    power = 1
    total = len(country_number) ** power
    # n이 몇자리의 124나라의 숫자로 나오는지 확인한다. 지수에 해당하는 자릿수를 갖는다.
    while n > total:
        power += 1
        total += len(country_number) ** power
    # p개의 요소를 가지는 순열에서 n번째에 해당하는 조합이 124나라의 숫자이다.
    A = [0] * power
    n -= total - len(country_number) ** power
    permutation_with_repetition([1, 2, 4], power, n)
    return ''.join(map(str, answer))


########################################
def solution1(n):
    country_number = [1, 2, 4]
    power = 1
    total = len(country_number) ** power
    while n > total:
        power += 1
        total += len(country_number) ** power
    n -= total - len(country_number) ** power
    n -= 1
    answer = ''
    while n:
        answer = str(country_number[n % len(country_number)]) + answer
        n //= len(country_number)
    if n == 0:
        for _ in range(power - len(answer)):
            answer = '1' + answer

    return answer
#################
# there is a more easier way.


if __name__ == "__main__":
    visited = [False] * 4
    # A = []
    # cnt = 0
    # answer = []
    # perm([1,2,3, 4])
    stack = [0] * 4
    print(solution(26))
