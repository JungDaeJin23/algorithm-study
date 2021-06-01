# brute force? check every time one is found. But 1000 by 1000 array is too big..
# pruning, is_promising?
# check from the biggest one?
# another way? 1의 갯수로 어느정도 짐작할 수 있지 않을까?
# similar to longest palindrome?
# swea 약품 보관함 크기 문제?
# _|으로 검사하면서 1 x


# 처음 나온 최대 길이 만큼 행 검사를 한다. 만약 행의 길이가 줄어들면 그 값이 여전히 최대 행보다 긴지 확인한다.
def search_biggest_one(board, i, j, length, longest_length):
    # bondary 까지 길이를 구한 뒤 여전히 최대 길이보다 긴지 확인한다.
    # while length > longest_length and len(board) - i >= length:
    if len(board) - i >= length:
        cmp_i = i + 1
        while cmp_i < i + length:
            cmp_j = j - length
            cmp_length = 0
            while cmp_j < j:
                if board[cmp_i][cmp_j]:
                    cmp_length += 1
                else:
                    length = cmp_length if cmp_length > (cmp_i - i) else cmp_i - i
                    break
                cmp_j += 1
            cmp_i += 1
        if length > longest_length:
            return length
    else:
        cmp_i = i + 1
        while cmp_i < len(board) and cmp_i < i + length:
            cmp_j = j - length
            cmp_length = 0
            while cmp_j < j:
                if board[cmp_i][cmp_j]:
                    cmp_length += 1
                else:
                    length = cmp_length if cmp_length > (cmp_i - i) else cmp_i - i
                    break
                cmp_j += 1
            cmp_i += 1
        if length > cmp_i - i:
            length = cmp_i - i
        if length > longest_length:
            return length
    return longest_length


# find;look for the longest line in a row major search
def solution(board):
    is_continuous = False
    longest_length = 0
    length = 0

    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):

            if board[i][j]:
                if is_continuous:
                    length += 1
                else:
                    is_continuous = True
                    length = 1
                # boundary condition
                if j == len(board[i]) - 1:
                    longest_length = search_biggest_one(board, i, j+1, length, longest_length)
                    length = 1
            else:
                is_continuous = False
                if length > longest_length:
                    # find the biggest square in this case
                    longest_length = search_biggest_one(board, i, j, length, longest_length)
                    length = 1
            j += 1
        i += 1

    return longest_length ** 2


if __name__ == "__main__":
    pass
    # print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
    # print(solution([[0,0,1,1],[1,1,1,1]]))
    # print(solution([[1,0],[0,1],[0,1]]))
    # print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    # print(solution([[1, 1, 1, 1], [1, 1, 1, 1]]))
    # print(solution([[1, 0], [1, 1], [1, 0], [1, 0]]))


# O(n)으로 할 방법은..
def find_longest_length(board, i, j, longest_length):
    shortest_width = 1000

    height = 0
    while i + height < len(board) and board[i + height][j] and height < shortest_width:
        width = 0
        while j + width < len(board[i + height]) and board[i + height][j + width]:
            width += 1
        board[i + height][j] = width
        if width < shortest_width:
            shortest_width = width
            if shortest_width <= longest_length:
                return longest_length
        height += 1
    if height <= longest_length:
        return longest_length
    return height


def solution(board):
    is_continuous = False
    longest_length = 0

    i = 0
    while i < len(board) - longest_length:
        j = 0
        while j < len(board[i]) - longest_length:
            if board[i][j]:
                if board[i][j]:
                    longest_length = find_longest_length(board, i, j, longest_length)
                elif board[i][j] > longest_length:
                    longest_length = find_longest_length(board, i, j, longest_length)
                    j += longest_length - 1
            j += 1
        i += 1
    return longest_length ** 2


if __name__ == "__main__":
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
    print(solution([[0,0,1,1],[1,1,1,1]]))
    print(solution([[1,0],[0,1],[0,1]]))
    print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[1, 1, 1, 1], [1, 1, 1, 1]]))
    print(solution([[0,0,0]]))
    print(solution([[0,1,0]]))


# stack dfs? pass

def solution(board):
    longest_length = 0

    i = 0
    while i < len(board) - longest_length:
        j = 0
        while j < len(board[i]) - longest_length:
            if board[i][j]:
                if board[i][j]:
                    pass
            j += 1
        i += 1
    return longest_length ** 2


if __name__ == "__main__":
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
    print(solution([[0,0,1,1],[1,1,1,1]]))
    print(solution([[1,0],[0,1],[0,1]]))
    print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[1, 1, 1, 1], [1, 1, 1, 1]]))
    print(solution([[0,0,0]]))
    print(solution([[0,1,0]]))
