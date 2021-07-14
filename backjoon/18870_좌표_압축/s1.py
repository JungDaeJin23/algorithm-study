# 수직선 위에 N개의 좌표 X1, X2, ..., XN이
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
N = int(input())
arr = list(map(int, input().split()))
set_arr = set(arr)
single_el_arr = sorted(list(set_arr))
for idx in range(len(single_el_arr)):
    for j in range(len(arr)):
        if arr[j] == single_el_arr[idx]:
            arr[j] = idx
print(*arr)