Country_1, Country_2, Country_3, Country_4 = input().split()
Board = list()
answer = list()
for _ in range(6):
    # A와 B가 경기를 진행했을 때 A가 승리할 확률은 W, 비길 확률은 D, 질 확률은 L이라는 의미이다.
    # W, D, L은 최대 소수점 세 자리까지 주어지며, W + D + L = 1이 보장
    A, B, W, D, L = input().split()
    Board.append([A, B, float(W), float(D), float(L)])


def sol(a=list()):
    global Board, answer
    if len(a) == len(Board):

        return

    for idx in range(2, 5):
        a.append(idx)
        sol(a)
        a.pop(-1)


sol()
for ans in answer:
    print(ans)