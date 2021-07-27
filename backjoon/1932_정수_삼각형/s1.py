N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
for idx in range(1, len(triangle)):
    for jdx in range(len(triangle[idx])):
        left = jdx - 1
        right = jdx
        if 0 <= left and right < len(triangle[idx]) - 1:
            if triangle[idx-1][left] > triangle[idx-1][right]:
                triangle[idx][jdx] += triangle[idx-1][left]
            else:
                triangle[idx][jdx] += triangle[idx - 1][right]
        elif jdx == 0:
            triangle[idx][jdx] += triangle[idx-1][jdx]
        else:
            triangle[idx][jdx] += triangle[idx-1][left]

print(max(triangle[-1]))