
def scissors_rock_paper(cards, i, j):
    i -= 1
    j -= 1
    if cards[i] == cards[j]:
        return i + 1
    elif cards[i] == 1:
        if cards[j] == 2:
            return j + 1
        else:
            return i + 1
    elif cards[i] == 2:
        if cards[j] == 3:
            return j + 1
        else:
            return i + 1
    elif cards[i] == 3:
        if cards[j] == 1:
            return j + 1
        else:
            return i + 1
    else:
        pass
# input and output
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # 1: 가위 2: 바위 3: 보 숫자가 같으면 번호가 작은 쪽인 승자

    # divide rule
    # recursion
    def divide_group(cards, i=1, j=len(cards)):
        if j - i == 1:
            winner = scissors_rock_paper(cards, i , j)
            return winner
        elif i == j:
            return i

        w1 = divide_group(cards, i=i, j=(i+j)//2)
        w2 = divide_group(cards, i=(i+j)//2+1, j=j)
        return scissors_rock_paper(cards, w1, w2)
    answer = divide_group(cards)

    print("#{0} {1}".format(tc, answer))
