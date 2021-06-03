T = int(input())

for tc in range(1, T+1):
    color_map = [[0]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        # color = 1(빨강), color = 2(파랑) 보라 >= 3
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if color_map[row][col] != color:
                    color_map[row][col] += color
    cnt = 0
    for i in range(10):
        for j in range(10):
            if color_map[i][j] >= 3:
                cnt += 1

    print('#{0} {1}'.format(tc, cnt))
