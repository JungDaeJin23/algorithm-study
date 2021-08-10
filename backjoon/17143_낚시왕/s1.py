R, C, M = map(int, input().split())
fishing_hole = [[0]*C for _ in range(R)]
sharks = []
for idx in range(M):
    # (r, c), s = speed, d = direction, z = size
    #      위,아래,오른쪽,왼쪽
    # d = [1, 2, 3, 4]
    # 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))
    fishing_hole[r-1][c-1] = (z, idx)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
# fishing
king_of_fishing = 0
# moving
for col in range(C):
    # fishing
    for row in range(R):
        if fishing_hole[row][col]:
            king_of_fishing += fishing_hole[row][col][0]
            sharks[fishing_hole[row][col][1]] = 0
            break
    # shark moves
    for idx in range(M):
        if sharks[idx] == 0:
            continue
        r, c, s, d, z = sharks[idx]
        # s
        for _ in range(s):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                else:
                    d = 3
                nr = r + dr[d]
                nc = c + dc[d]
            r = nr
            c = nc
        sharks[idx] = (r, c, s, d, z)

    # shark eat
    fishing_hole = [[0]*C for _ in range(R)]
    tmp = []
    for idx in range(M):
        if sharks[idx] == 0:
            continue
        r, c, s, d, z = sharks[idx]
        if fishing_hole[r][c]:
            if fishing_hole[r][c][0] > z:
                tmp.append(idx)
            else:
                tmp.append(fishing_hole[r][c][1])
                fishing_hole[r][c] = (z, idx)
        else:
            fishing_hole[r][c] = (z, idx)
    for idx in tmp:
        sharks[idx] = 0
print(king_of_fishing)


