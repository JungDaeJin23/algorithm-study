def my_factorial(n):
    if n <= 1:
        return 1
    return n * my_factorial(n-1)


def sol(n):
    a = 10
    b = 20
    cnt = 0

    max_b_cnt = n // b
    for i in range(max_b_cnt + 1):
        j = (n - b*i) // a
        cnt += my_factorial(i + j) // (my_factorial(i) * my_factorial(j)) * 2**i
    return cnt


# input and output
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print("#{0} {1}".format(tc, sol(N)))
