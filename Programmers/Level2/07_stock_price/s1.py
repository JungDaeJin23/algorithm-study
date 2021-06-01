# Use stack


def solution(prices):
    stack = prices[:]
    top = -1
    answer = prices[:]

    # time == idx
    for time, price in enumerate(prices):
        if top == -1:  # is_empty
            top += 1
            stack[top] = (price, time)
        else:
            # 한번만 비교하고 말아서 틀렸었다.
            # cmp_price, cmp_time = stack[top]
            # if price >= cmp_price:
            #     top += 1
            #     stack[top] = (price, time)
            # else:
            #     while True:
            #         answer[cmp_time] = time - cmp_time
            #         stack[top] = (price, time)
            # 조건이 만족한다면 한개가 아니라 stack top == -1 까지 비교해야됨
            while top != -1:
                cmp_price, cmp_time = stack[top]
                if price >= cmp_price:
                    top += 1
                    stack[top] = (price, time)
                    break
                else:
                    answer[cmp_time] = time - cmp_time
                    top -= 1
            else:
                top += 1
                stack[top] = (price, time)

    max_time = len(prices) - 1
    while top != -1:
        price, time = stack[top]
        top -= 1
        answer[time] = max_time - time

    return answer
"""
테스트 1 〉	통과 (25.62ms, 18.6MB)
테스트 2 〉	통과 (19.11ms, 17.4MB)
테스트 3 〉	통과 (28.86ms, 19.8MB)
테스트 4 〉	통과 (22.00ms, 18MB)
테스트 5 〉	통과 (17.29ms, 17.5MB)
"""

#################################
# solved in the past O(n^2)?
# def solution(prices):
#     answer = [0] * len(prices)
#
#     for i_idx in range(len(prices)):
#         for j_idx in range(i_idx + 1, len(prices)):
#             if prices[i_idx] > prices[j_idx] or j_idx == len(prices) - 1:
#                 answer[i_idx] = j_idx - i_idx
#                 break
#
#     return answer
"""
테스트 1 〉	통과 (182.10ms, 18.7MB)
테스트 2 〉	통과 (140.43ms, 17.5MB)
테스트 3 〉	통과 (224.88ms, 19.5MB)
테스트 4 〉	통과 (162.58ms, 18.2MB)
테스트 5 〉	통과 (121.10ms, 17MB)
"""


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
