# 1 ≤ N ≤ 4,000,000
def combine(n, k):
    global memo
    if k > n//2:
        k = n - k
    if k == 0:
        return 1
    # if n == k:
    #     return 1
    if n < 10000:
        if memo[n][k] == 0:
            memo[n][k] = combine(n-1, k-1) + combine(n-1, k)
        return memo[n][k]
    return combine(n-1, k-1) + combine(n-1, k)

if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(4000000)
    N, K = map(int, input().split())
    memo = [[0]*(i//2) for i in range(2, 10000)]
    ans = combine(N, K) % 1000000007
    print(ans)