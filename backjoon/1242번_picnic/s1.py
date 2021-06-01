# 즐?
# N: total, K: quit order, M: position
# 1 <= N, K <= 5,000,000
# 1. simulation, visited_list, circular queue
# 2. 두개의 큐를 사용해서 data size 를 줄인다. 하나의 큐에서 가능할듯, 일단 두개로
# 3. 원형큐로  N + 1 사이즈로 만들고 퇴출 안당한 번호는 rear 로 옮긴다. resizing

# 1.
# N, K, M = map(int, input().split())
# knock_out_list = [False] * (N + 1)
# knock_out_list[0] = True
# left_player = N
# cnt = 0
# idx = 0

# while not knock_out_list[M]:
#     k = K % left_player
#     cnt += 1
#     while k:
#         idx = (idx + 1) % (N + 1)
#         if not knock_out_list[idx]:
#             k -= 1
#     knock_out_list[idx] = True
#     left_player -= 1
# print(cnt)

# 2.
# N, K, M = map(int, input().split())
# players = [i for i in range(1, N + 1)]
# tmp = [0] * N
# left_player = N
# cnt = 0
# i =  0
# j = 0
# while True:
#     k = K % left_player
#     cnt += 1
#     for _ in range(k):
#

N, K, M = map(int, input().split())
cq = [i for i in range(N + 1)]
front = 0
rear = N
left_player = N  # == rear - front?
cnt = 0

while True:
    k = K % left_player
    cnt += 1
    for _ in range(k):
        front = (front + 1) % (N + 1)
        rear = (rear + 1) % (N + 1)
        cq[rear] = cq[front]

    if cq[rear] == M:
        break
    left_player -= 1
    if rear:
        rear -= 1
    else:
        rear = N
print(cnt)
