# 입력으로 N 개의 상자들의 가로, 세로, 높이의 길이가 각각 주어질 때,
# 쌓을 수 있는 최대 높이를 계산하는 프로그램을 작성하라.
# N 개의 상자를 쌓는 순서에는 별다른 제약이 없으며, 모든 상자를 다 사용하지 않아도 된다.
T = int(input())
# 1. Brute force: 3^N
#  N 은 2 이상 20 이하의 정수이다. (2 ≤ N ≤ 20)
# 9^10 < 10^10 = 1000 * 1000 * 1000 * 10
def backtracking(height=0, width=10000, depth=10000):
    global max_height, boxes, used
    if height > max_height:
        max_height = height
    for i in range(len(boxes)):
        if used[i] == 0:
            used[i] = 1
            tmp = boxes[i]
            w, d, h = tmp[0], tmp[1], tmp[2]
            if w <= width and d <= depth:
                backtracking(height=height+h, width=w, depth=d)
            elif w <= depth and d <= width:
                backtracking(height=height + h, width=d, depth=w)
            w, d, h = tmp[2], tmp[0], tmp[1]
            if w <= width and d <= depth:
                backtracking(height=height+h, width=w, depth=d)
            elif w <= depth and d <= width:
                backtracking(height=height + h, width=d, depth=w)
            w, d, h = tmp[1], tmp[2], tmp[0]
            if w <= width and d <= depth:
                backtracking(height=height+h, width=w, depth=d)
            elif w <= depth and d <= width:
                backtracking(height=height + h, width=d, depth=w)
            used[i] = 0


for tc in range(1, T+1):
    N = int(input())
    # 두 번째 줄 부터는 각각의 상자들의 가로 width, 세로 depth, 높이 height 길이가 나열된다.
    boxes = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*len(boxes)
    max_height = 0
    backtracking()

    print('#{0} {1}'.format(tc, max_height))
