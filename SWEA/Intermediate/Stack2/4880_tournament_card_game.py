T = int(input())
# 카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.


def get_winner(i, j):
    global players
    if players[i] == [j]:
        return i
    elif players[i] == 1:
        if players[j] == 2:
            return j
        return i
    elif players[i] == 2:
        if players[j] == 3:
            return j
        return i
    else:
        if players[j] == 1:
            return j
        return i


def RSP_simulation(i, j):
    if i == j:
        return i

    if j-i == 1:
        return get_winner(i, j)
    winner1 = RSP_simulation(i, (i+j)//2)
    winner2 = RSP_simulation((i+j)//2+1, j)
    return get_winner(winner1, winner2)


for tc in range(1, T+1):
    N = int(input())
    players = [0] + list(map(int, input().split()))

    print('#{0} {1}'.format(tc, RSP_simulation(1, N)))
