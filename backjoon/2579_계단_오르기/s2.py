#계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다. -> 뒤에서 부터 or 마지막 전전과 전을 동시에 밟으면 안된다.
# 마지막 계단은 연속되어서 올라온 값을 제외해야 함으로 따로 빼준다. or stairs 에 빈 공간 append
# 계단의 개수는 300이하의 자연수
N = int(input())
stairs = [int(input()) for _ in range(N)]
ans = 0

# Way 3. greedy X 모든 순간의 최선의 선택이 최고의 결과를 만들지 않는다.
flag = False
idx = len(stairs)-1
ans += stairs[idx]
while idx > 0:
    idx -= 1
    if flag:
        if idx == 0:
            break
        idx -= 1
        bigger_one_idx = idx
    else:
        if idx == 0:
            bigger_one_idx = idx
        else:
            if stairs[idx] >= stairs[idx-1]:
                bigger_one_idx = idx
                flag = True
            else:
                idx -= 1
                bigger_one_idx = idx
                flag=False
    ans += stairs[bigger_one_idx]

print(ans)

