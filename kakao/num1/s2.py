def follow_rule(place, row, col, original_point, dis=1):
    if dis > 2:
        return True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5 and original_point != (nr, nc):
            if place[nr][nc] == 'P':
                return False
            elif place[nr][nc] == 'O':
                # 아직은 모름 return 하면 안됨
                if not follow_rule(place, nr, nc, original_point, dis=dis+1):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        flag = False
        for row in range(len(place)):
            for col in range(len(place[row])):
                if place[row][col] == 'P' and not follow_rule(place, row, col, (row, col)):
                    flag = True
                    break
            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer

if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


def solution1(places):
    dr = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
    dc = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]
    answer = []
    # 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
    for place in places:
        flag = False
        for i in range(len(places)):
            for j in range(len(places[i])):
                if place[i][j] == 'P':
                    for d in range(len(dr)):
                        nr = i + dr[d]
                        nc = j + dc[d]
                        if 0 <= nr < 5 and 0 <= nc < 5:
                            if place[nr][nc] == 'P':
                                flag = True
                                break
                        if flag:
                            break
                if flag:
                    break
            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
