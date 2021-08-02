T = input()
P = input()
return_position = [0] * len(P)
cnt = 0
ans = []
# 전처리
idx = 1
while idx < len(P):
    jdx = 0
    while idx < len(P) and P[idx] == P[jdx]:
        return_position[idx] = jdx + 1
        idx += 1
        jdx += 1
    idx += 1
print(return_position)
idx = 0
jdx = 0
while idx < len(T) - len(P) + 1:
    while jdx < len(P):
        if T[idx + jdx] != P[jdx]:
            if jdx > 0:
                jdx -= 1
            idx += jdx - return_position[jdx]
            jdx = 0
            break
        jdx += 1
    else:
        jdx = 0
        cnt += 1
        ans.append(idx+1)
    idx += 1

print(cnt)
print(*ans)