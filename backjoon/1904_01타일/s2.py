# 모듈로 연산?
N = int(input())
tile = [0, 1, 2, 3, 5]
while len(tile) <= N:
    tile.append((tile[-1] + tile[-2])%15746)
print(tile[N])