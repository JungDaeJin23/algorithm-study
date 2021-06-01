# bit operator?
# greedy?
# 첫자리부터 k 번째까지중에서 가장 큰 수가 오는 자리까지만 수를 제한다. xxxxxx
# 맨 앞부터 두자리씩 비교하는데 더 큰 수가 뒤에 올 경우 앞을 제거한다. 스택을 사용하자


def solution(number: str, k: int) -> str:
    stack = [0] * len(number)
    top = -1

    idx = 0
    while k and idx < len(number):
        if top == -1:
            top += 1
            stack[top] = int(number[idx])
        else:
            # 한 번이 아니라 끝까지 비교 while 사용해야됨
            while k and top != -1:
                cmp_num = stack[top]
                if cmp_num < int(number[idx]):
                    top -= 1
                    k -= 1
                else:
                    top += 1
                    stack[top] = int(number[idx])
                    break
            else:  # k == 0 or top == -1
                top += 1
                stack[top] = int(number[idx])
        idx += 1
    answer = ''
    if k:
        top -= k
    while top != -1:
        answer = str(stack[top]) + answer
        top -= 1
    for i in range(idx, len(number) - k):
        answer = answer + number[i]
    return answer
# 다른 사람 코드 순회를 끝냈는데 k가 남았을 경우 마이너스 슬라이싱 요소로 사용했다.
# if k != 0:
#         stack = stack[:-k]

if __name__ == "__main__":
    print(solution("1231234", 3))
    print(solution("1924321", 3))  # 9432
    print(solution("4177252841", 4))  # 775841
    print(solution("11119", 3))  # 19
