# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문
#  NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
def sol(N, M, matrix):
    palindrome = ''
    repetition = N - M + 1
    palindrome_index = [(t, M - 1 - t) for t in range(M // 2)]
    for i in range(N):
        for j in range(repetition):
            for front, back in palindrome_index:
                if matrix[i][j + front] != matrix[i][j + back]:
                    break
            else:
                return matrix[i][j:j + M]

            for front, back in palindrome_index:
                if matrix[j+front][i] != matrix[j+back][i]:
                    palindrome = ''
                    break
            else:
                for k in range(M):
                    palindrome += matrix[j + k][i]
                return palindrome


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    print('#{0} {1}'.format(tc, sol(N, M, matrix)))
