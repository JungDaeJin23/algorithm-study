N, K = map(int, input().split())
factorial_list = [1, 1, 2, 6]

def my_factorial(n):
    global factorial_list
    while len(factorial_list) <= n:
        factorial_list.append(factorial_list[len(factorial_list)-1]*len(factorial_list))
    return factorial_list[n]
ans = my_factorial(N) // (my_factorial(N-K) * my_factorial(K))
print(ans%1000000007)