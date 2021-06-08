# backtracking을 사용한 power set
# 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합


def construct_cadidates(a, k, input1, c):
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    print("(", end='')
    for i in range(k+1):
        if a[i]:
            print(i, end=' ')
    print(")")


def backtrack(a, k, input1):
    global MAXCADAIDATES
    c = [0]*MAXCADAIDATES

    if k == input1:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_cadidates(a, k, input1, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input1)
A = [i for i in range(10)]
MAXCADAIDATES = 100
NMAX = 100
a = [0]*NMAX
backtrack(a, 0, 4)
