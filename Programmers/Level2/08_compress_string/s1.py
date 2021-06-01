# stack, queue brute force
# Compare until compression contains a half-length string; compare until compression have half length of string


def solution(s):
    stack = [''] * len(s)
    top = -1

    queue = list(s)
    front = -1
    rear = len(queue) - 1

    answer = len(s)

    unit = 1
    while unit <= len(s) // 2:
        if top == -1:
            top += 1
            # stack[top] = (0, ''.join(queue[front + 1: front + 1 + unit]))
            # 문자열도 인덱스 넘어간거는 상관없음. 최댓값으로 계산해서 반환. front + 1 + unit > len(s) - 1 비교 불필요
            # 0으로 하고 if repetition으로 하려고 했는데 그러면 숫자 가해줄 때 복잡해져서 값을 1로 바꿔줌
            stack[top] = (1, s[front + 1: front + 1 + unit])
            front += unit
        else:
            repetition, compression_string = stack[top]
            if s[front + 1: front + 1 + unit] == compression_string:
                stack[top] = (repetition + 1, compression_string)
            else:
                top += 1
                stack[top] = (1, s[front + 1: front + 1 + unit])
            front += unit

        if front >= rear:
            compressed_s = ''
            while top != -1:
                repetition, compression_string = stack[top]
                if repetition > 1:
                    compressed_s = compressed_s + str(repetition) + compression_string
                else:
                    compressed_s = compressed_s + compression_string
                top -= 1
            if len(compressed_s) < answer:
                answer = len(compressed_s)
            front = -1
            unit += 1
    return answer


if __name__=="__main__":
    print(solution("ababcdcdababcdcd"))  # 9
    print(solution("abcabcdede"))  # 8
    print(solution("abcabcabcabcdededededede"))  # 14
    print(solution("xababcdcdababcdcd"))  # 17
    print(solution("xxxxxxxxxxyyy"))  # 5
