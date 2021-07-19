T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    print('#{0} {1}'.format(tc, queue[M%N]))