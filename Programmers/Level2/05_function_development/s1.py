# linear queue


def solution(progresses, speeds):
    cnt = 0
    stack = [0] * len(progresses)
    top = -1
    # progresses queue
    front = -1
    rear = len(progresses) - 1

    while front != rear:  # is_empty
        cnt = 0

        # plus speed until front progress is under 100
        while progresses[front + 1] < 100:
            for idx in range(front + 1, rear + 1):
                progresses[idx] += speeds[idx]

        # deque items finished progress
        while front != rear and progresses[front + 1] >= 100:
            front += 1
            cnt += 1

        if cnt:
            top += 1
            stack[top] = cnt
    return stack[0:top + 1]


#################
# solved in the past
# def solution(progresses, speeds):
    # answer = []
    # while progresses:
    #     progresses = [progresses[idx] + speeds[idx] for idx in range(len(progresses))]
    #     for idx, val in enumerate(progresses):
    #         if val < 100:
    #             break
    #     else:
    #         return answer + [len(progresses)]
    #     progresses, speeds = progresses[idx:], speeds[idx:]
    #     if idx:
    #         answer.append(idx)
    #
    # return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
