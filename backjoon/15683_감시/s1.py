N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = N * M
CCTV = []
for row in range(N):
    for col in range(M):
        if 1 <= Map[row][col] <= 5:
            CCTV.append((Map[row][col], row, col))


def sol(m, cctv, cnt=0):
    global N, M, answer, dr, dc
    if len(cctv) == cnt:
        tmp = 0
        for row in range(N):
            for col in range(M):
                if m[row][col] == 0:
                    tmp += 1
        if tmp < answer:
            answer = tmp
        return

    if cctv[cnt][0] in [1, 3, 4]:
        if cctv[cnt][0] == 1:
            for d in range(4):
                duplicated_map = []
                for row in range(N):
                    duplicated_map.append(m[row][:])

                nr = cctv[cnt][1] + dr[d]
                nc = cctv[cnt][2] + dc[d]
                while True:
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or m[nr][nc] == 6:
                        break
                    if m[nr][nc] in [1, 2, 3, 4, 5]:
                        pass
                    else:
                        duplicated_map[nr][nc] = '#'
                    nr += dr[d]
                    nc += dc[d]
                sol(duplicated_map, cctv, cnt=cnt + 1)
        elif cctv[cnt][0] == 3:
            for d in range(4):
                duplicated_map = []
                for row in range(N):
                    duplicated_map.append(m[row][:])
                ar = [(-1, 0), (1, 0), (1, 0), (-1, 0)]
                ac = [(0, 1), (0, 1), (0, -1), (0, -1)]
                for t in range(2):
                    nr = cctv[cnt][1] + ar[d][t]
                    nc = cctv[cnt][2] + ac[d][t]
                    while True:
                        if nr < 0 or nr >= N or nc < 0 or nc >= M or m[nr][nc] == 6:
                            break
                        if m[nr][nc] in [1, 2, 3, 4, 5]:
                            pass
                        else:
                            duplicated_map[nr][nc] = '#'
                        nr += ar[d][t]
                        nc += ac[d][t]
                sol(duplicated_map, cctv, cnt=cnt + 1)
        else:
            for d in range(4):
                duplicated_map = []
                for row in range(N):
                    duplicated_map.append(m[row][:])

                for t in range(3):
                    idx = d + t
                    if idx >= 4:
                        idx -= 4
                    nr = cctv[cnt][1] + dr[idx]
                    nc = cctv[cnt][2] + dc[idx]
                    while True:
                        if nr < 0 or nr >= N or nc < 0 or nc >= M or m[nr][nc] == 6:
                            break
                        if m[nr][nc] in [1, 2, 3, 4, 5]:
                            pass
                        else:
                            duplicated_map[nr][nc] = '#'
                        nr += dr[idx]
                        nc += dc[idx]
                sol(duplicated_map, cctv, cnt=cnt + 1)
    elif cctv[cnt][0] == 2:
        for d in [0, 2]:
            duplicated_map = []
            for row in range(N):
                duplicated_map.append(m[row][:])

            for t in range(2):
                nr = cctv[cnt][1] + dr[d+t]
                nc = cctv[cnt][2] + dc[d+t]
                while True:
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or m[nr][nc] == 6:
                        break
                    if m[nr][nc] in [1, 2, 3, 4, 5]:
                        pass
                    else:
                        duplicated_map[nr][nc] = '#'
                    nr += dr[d+t]
                    nc += dc[d+t]
            sol(duplicated_map, cctv, cnt=cnt + 1)
    else:
        duplicated_map = []
        for row in range(N):
            duplicated_map.append(m[row][:])

        for d in range(4):
            nr = cctv[cnt][1] + dr[d]
            nc = cctv[cnt][2] + dc[d]
            while True:
                if nr < 0 or nr >= N or nc < 0 or nc >= M or m[nr][nc] == 6:
                    break
                if m[nr][nc] in [1, 2, 3, 4, 5]:
                    pass
                else:
                    duplicated_map[nr][nc] = '#'
                nr += dr[d]
                nc += dc[d]
        sol(duplicated_map, cctv, cnt=cnt+1)


sol(Map, CCTV)

print(answer)