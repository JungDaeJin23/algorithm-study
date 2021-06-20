N = int(input())
star_matrix = [['*']*N for _ in range(N)]


def print_star_recursion(n, repetition=1):
    global star_matrix, N
    if n >= 1:
        end = 2*n
        idx = jdx = 0
        for _ in range(repetition):
            jdx = 0
            for _ in range(repetition):
                for row in range(n + idx, end + idx):
                    for col in range(n + jdx, end + jdx):
                        star_matrix[row][col] = ' '
                jdx += n*3
            idx += n*3
        print_star_recursion(n//3, repetition=repetition*3)


print_star_recursion(N//3)
for line in star_matrix:
    print(''.join(line))
