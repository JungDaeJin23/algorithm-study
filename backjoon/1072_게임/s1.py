# 게임 횟수 : X
# 이긴 게임 : Y (Z%)
# 첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.
X, Y = map(int, input().split())
Z = Y * 100 // X
before_Z = Z
cnt = 0
if Z == 100:
    cnt = -1

while before_Z == Z < 100:
    cnt += 1
    X += 1
    Y += 1
    Z = Y * 100 // X
    # print(cnt)
print(cnt)