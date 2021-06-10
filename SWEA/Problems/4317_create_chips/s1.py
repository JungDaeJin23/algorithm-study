T = int(input())
# 최대 생산 가능한 칩의 개수를 출력하는 프로그램
# 하나의 칩을 생산하기 위해서는 웨이퍼에서 2*2 영역이 필요
for tc in range(1, T+1):
    H, W = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(H)]

    print('#{0} {1}'.format(tc, ))
