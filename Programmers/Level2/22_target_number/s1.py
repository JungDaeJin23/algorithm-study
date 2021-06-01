# dfs 더하는 경우 빼는 경우 두가지를 담는다.
# 마지막에 target과 같으면 + 1


def DFS(numbers, target, total=0, idx=0):
    global answer
    if idx == len(numbers):
        if total == target:
            answer += 1
        return None

    total += numbers[idx]
    DFS(numbers, target, total, idx + 1)
    total -= 2 * numbers[idx]
    DFS(numbers, target, total, idx + 1)

    return None

def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers, target)
    return answer

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1],	3))  # 5
