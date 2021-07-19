# 2. 포기
# 내림차순이 유지되는 구간은 전부 동일한 값을 갖는다. -1 제외
# 뒤에서 부터 탐색하면 오름차순 (greater than or equal)
# 같은 값을 가지는 구간을 저장한다.
N = int(input())
arr = list(map(int, input().split()))
nge = [-1] * N
idx = len(arr)-1
# 값이 작아지면 nge 값 갱신
if arr[idx-1] < arr[idx]:
    max_ = arr[idx]
    nge[idx-1] = max_
idx -= 1
# 왼쪽으로 갈 수록 크거나 같으면서 최댓값보다 작으면 계속 최댓값으로 갱신
while arr[idx-1] >= arr[idx]:
    nge[idx-1] = max_
    break