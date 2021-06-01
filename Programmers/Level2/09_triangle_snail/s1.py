# 바로 떠오른 것 가변 리스트 사용해서 삼각형을 펼쳐서 2차원 리스트에 사각형 형식에 맞춰서 넣는다.
# delta direction은 잘 모르겠다.
#  양쪽에서 집어넣는 큐?
# def solution(n):
#     # (arr, front, rear)
#     triangle_matrix = [([0] * (i + 1), -1, i) for i in range(n)]
#     idx = 0
#     num = 1
#     while True:
#         arr, front, rear = triangle_matrix[idx]
#         arr[front + 1] = num
#         front += 1
#         triangle_matrix[idx] = (arr, front, rear)
#         idx += 1
#         num += 1


# delta direction
def solution(n):
    if n == 1:
        return [1]
    triangle_matrix = [[0] * (i + 1)for i in range(n)]
    # down, right, up reverse diagonal
    row = col = 0
    dr = [1, 0, -1]
    dc = [0, 1, -1]

    d = 0
    num = 1
    while not triangle_matrix[row][col]:
        triangle_matrix[row][col] = num
        row += dr[d]
        col += dc[d]
        num += 1

        if row >= n or col >= n or triangle_matrix[row][col]:
            row -= dr[d]
            col -= dc[d]
            d = (d + 1) % 3
            row += dr[d]
            col += dc[d]
    answer = []
    for triangle_list in triangle_matrix:
        answer.extend(triangle_list)
    # return sum(triangle_matrix, [])
    return answer



if __name__ == "__main__":
    print(solution(1))
