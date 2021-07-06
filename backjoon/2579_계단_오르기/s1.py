#계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다. -> 뒤에서 부터 or 마지막 전전과 전을 동시에 밟으면 안된다.
# 계단의 개수는 300이하의 자연수
# 시간 초과
N = int(input())
stairs = [int(input()) for _ in range(N)]
ans = 0
# Way 1. brute force X


# Way 2. DP, bitmask를 통한 개선 가능성?
def count_stairs(now_stair, score=0, is_in_a_row=False):
    global ans, stairs
    if now_stair < 0:
        return

    score += stairs[now_stair]
    if score > ans:
        ans = score

    if is_in_a_row:
        count_stairs(now_stair - 2, score=score, is_in_a_row=False)
    else:
        count_stairs(now_stair - 1, score=score, is_in_a_row=True)
        count_stairs(now_stair - 2, score=score, is_in_a_row=False)

    return


count_stairs(len(stairs)-1)
print(ans)
