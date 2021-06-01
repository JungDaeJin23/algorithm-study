# 밑에서 위로 탐색 column major
def down_block(board):
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[len(board) -1 - row][col] == '':
                k = 1
                flag = False
                while len(board) -1 - row - k != -1:
                    if board[len(board) -1 - row - k][col] != '':
                        flag = True
                        break
                    k += 1
                if flag:
                    board[len(board) - 1 - row][col] = board[len(board) -1 - row - k][col]
                    board[len(board) - 1 - row - k][col] = ''
    return board

def check_deleted_block(board):
    tmp = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            # 위 왼쪽 좌상
            dr = [-1, 0, -1]
            dc = [0, -1, -1]
            stack = 0
            temp = [(row, col), ]
            for d in range(3):
                nr = row + dr[d]
                nc = col + dc[d]
                # boundary condition
                if 0 <= nr < len(board) and 0 <= nc < len(board[row]):
                    if board[row][col] != '' and board[row][col] == board[nr][nc]:
                        if d < 2:
                            stack += 1
                            temp.append((nr, nc))
                        elif stack == 2:
                            temp.append((nr, nc))
                            tmp.extend(temp)
    return list(set(tmp))


# DP fail
def solution1(m, n, board):
    score_board = [[1]*len(board[0]) for _ in range(len(board))]
    tmp = []
    for row in range(m):
        for col in range(n):
            # 위 왼쪽 좌상
            dr = [-1, 0, -1]
            dc = [0, -1, -1]
            stack = 0
            for d in range(3):
                nr = row + dr[d]
                nc = col + dc[d]
                # boundary condition
                if 0 <= nr < m and 0 <= nc < n:
                    if board[row][col] == board[nr][nc]:
                        if d < 2:
                            score_board[row][col] += score_board[nr][nc]
                            stack += 1
                        elif stack == 2:
                            score_board[row][col] -= score_board[nr][nc]
                            tmp.append((row, col, board[row][col], score_board[row][col]))
    # for i in range(len(score_board)):
    #     print(score_board[i])
    # print(tmp)

    answer = 0
    return answer


def solution(m, n, board):
    board = [list(board[i]) for i in range(len(board))]
    answer = 0
    position_list = check_deleted_block(board)
    answer += len(position_list)
    for row, col in position_list:
        board[row][col] = ''
    board = down_block(board)
    while len(position_list):
        position_list = check_deleted_block(board)
        answer += len(position_list)
        for row, col in position_list:
            board[row][col] = ''
        board = down_block(board)
    return answer


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
