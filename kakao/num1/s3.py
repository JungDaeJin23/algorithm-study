# 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
# 원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.
def solution(n, k, cmd):
    linked_list = [(i, i+1, ) for i in range(n)]
    # (before_linked_idx, idx, next_linked_idx)
    deleted_stack = [(0, 0)] * n
    top = -1

    for command in cmd:
        if len(command) > 1:
            direction, num = command.split()
            num = int(num)
            if direction == 'U':
                pass
            else:
                pass
        else:
            if command == 'Z':
                top -= 1
            else:
                top += 1
                deleted_stack[top] = (k, linked_list[k])
                linked_list[k] = linked_list[linked_list[k]] + 1

    answer = ''
    return answer


if __name__ == "__main__":
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))



def solution1(n, k, cmd):
    deleted_stack = [0] * n
    top = -1

    for command in cmd:
        if len(command) > 1:
            direction, num = command.split()
            num = int(num)
            if direction == 'U':
                pass
            else:
                pass
        else:
            if command == 'Z':
                top -= 1
            else:
                top += 1
                deleted_stack[top] = k

    answer = ''
    return answer