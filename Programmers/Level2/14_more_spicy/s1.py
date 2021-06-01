# # Heap?
# # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# # 모든 음식의 스코빌 지수를 K 이상
# # counting list
# # scoville의 길이는 2 이상 1,000,000 이하입니다.
# # K는 0 이상 1,000,000,000 이하입니다.
# # 조건이 너무 크다 일단 보류
# # K 까지만 만들까? 그래도 시간 초과..
#
#
# def solution(scoville, K):
#     # K 가 넘어가는 숫자는 K에 저장한다.
#     scoville_count_list = [0] * (K + 1)  # 스코빌 지수가 0인 원소도 있다
#     cnt_under_K = 0
#     for idx in scoville:
#         if idx >= K:
#             scoville_count_list[K] += 1
#         else:
#             cnt_under_K += 1
#             scoville_count_list[idx] += 1
#
#     # 조건 나중에 일단 돌려보자
#     smallest_idx = 0
#     second_smallest_idx = 0
#     cnt = 0
#     while cnt_under_K > 1:
#         cnt += 1
#         while smallest_idx < len(scoville_count_list):
#             if scoville_count_list[smallest_idx]:
#                 scoville_count_list[smallest_idx] -= 1
#                 break
#             smallest_idx += 1
#         second_smallest_idx = smallest_idx
#         while second_smallest_idx < len(scoville_count_list):
#             if scoville_count_list[second_smallest_idx]:
#                 scoville_count_list[second_smallest_idx] -= 1
#                 break
#             second_smallest_idx += 1
#
#         new_idx = smallest_idx + 2 * second_smallest_idx
#         if new_idx >= K:
#             scoville_count_list[K] += 1
#             cnt_under_K -= 2
#         else:
#             scoville_count_list[new_idx] += 1
#             cnt_under_K -= 1
#     # cnt_under_K == 1 or 0
#     if cnt_under_K == 0:
#         return cnt
#     if scoville_count_list[K]:
#         return cnt + 1
#     return -1
#
# if __name__ == "__main__":
#     print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
#
#
# # 매번 정렬?
# # 정렬 하지 말고 가장 작은 값, 두번 째로 작은 값 산출
# # 가장 작은 게 K보다 작다면  계산하고 두 번째 작았던 자리에 넣어줌
# # 인덱스 1씩 늘려가면서 범위 줄임 x
# # 가장 작은 인덱스 위치에는 -1 넣어서 제외 시킨다.
# def solution(scoville, K):
#     smallest_idx = 0
#     second_smallest_idx = 0
#
#     # 1. 두 번 순회한다.
#     for idx in range(len(scoville)):
#         if scoville[idx] < scoville[smallest_idx]:
#             smallest_idx = idx
#     if second_smallest_idx == smallest_idx:
#         second_smallest_idx = 1
#     for idx in range(len(scoville)):
#         if idx != smallest_idx and scoville[idx] < scoville[second_smallest_idx]:
#             second_smallest_idx = idx
#     # print(smallest_idx, second_smallest_idx)
#
#     n = len(scoville)
#     while scoville[smallest_idx] < K:
#         # mix: new = x + 2y
#         new = scoville[smallest_idx] + 2 * scoville[second_smallest_idx]
#         scoville[smallest_idx] = -1
#         scoville[second_smallest_idx] = new
#         n -= 1
#
#         if n == 1:
#             if new >= K:
#                 return len(scoville) - 1
#             return -1
#
#         # 다시 검사
#         smallest_idx = None
#         second_smallest_idx = None
#         for idx, el in enumerate(scoville):
#             if 0 <= el:
#                 if not smallest_idx:
#                     smallest_idx = idx
#                 else:
#                     if scoville[idx] < scoville[smallest_idx]:
#                         smallest_idx = idx
#
#         for idx, el in enumerate(scoville):
#             if 0 <= el:
#                 if not second_smallest_idx:
#                     second_smallest_idx = idx
#                 else:
#                     if idx != smallest_idx and scoville[idx] < scoville[second_smallest_idx]:
#                         second_smallest_idx = idx
#     return len(scoville) - n
#
#
# if __name__ == "__main__":
#     print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
#
#
# # dictionary == 튜플(key, value) pair
# def solution(scoville, K):
#     scoville_hash = {K: 0}
#     cnt_under_K = 0
#     # scale 척도, index 지수
#     for scale in scoville:
#         if scale >= K:
#             scoville_hash[K] += 1
#         else:
#             if scoville_hash.get(scale):
#                 scoville_hash[scale] += 1
#             else:
#                 scoville_hash[scale] = 1
#             cnt_under_K += 1
#     cnt = 0
#     while cnt_under_K > 1:
#         cnt += 1
#         smallest_key = None
#         for key, val in scoville_hash.items():
#             if val:
#                 if not smallest_key:
#                     smallest_key = key
#                 elif key < smallest_key:
#                     smallest_key = key
#         scoville_hash[smallest_key] -= 1
#         if scoville_hash[smallest_key] == 0:
#             del scoville_hash[smallest_key]
#
#         second_smallest_key = None
#         for key, val in scoville_hash.items():
#             if val:
#                 if not second_smallest_key:
#                     second_smallest_key = key
#                 elif key < second_smallest_key:
#                     second_smallest_key = key
#         scoville_hash[second_smallest_key] -= 1
#         if scoville_hash[second_smallest_key] == 0:
#             del scoville_hash[second_smallest_key]
#
#         new_key = smallest_key + 2 * second_smallest_key
#         if new_key >= K:
#             scoville_hash[K] += 1
#             cnt_under_K -= 2
#         else:
#             if scoville_hash.get(new_key):
#                 scoville_hash[new_key] += 1
#             else:
#                 scoville_hash[new_key] = 1
#             cnt_under_K -= 1
#     # cnt_under_K == 1 or 0
#     if cnt_under_K == 0:
#         return cnt
#     # K == 1
#     if scoville_hash[K]:
#         return cnt + 1
#     return -1
#
# if __name__ == "__main__":
#     print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
#     print(solution(	[1, 1, 2, 2, 3, 3, 4, 4, 5], 7))  # 6
#
#
# # 매번 정렬
# def solution(scoville, K):
#     scoville.sort()
#     over_k_idx = len(scoville) - 1
#     while scoville[over_k_idx] >= K:
#         over_k_idx -= 1
#
#     start_idx = 0
#     cnt = 0
#     while scoville[start_idx] < K:
#         cnt += 1
#         new_scoville = scoville[start_idx] + 2 * scoville[start_idx + 1]
#         start_idx += 1
#         scoville[start_idx] = new_scoville
#         cmp_idx = start_idx
#         while cmp_idx < len(scoville) - 1:
#             if scoville[cmp_idx] > scoville[cmp_idx + 1]:
#                 scoville[cmp_idx], scoville[cmp_idx + 1] = scoville[cmp_idx + 1], scoville[cmp_idx]
#                 cmp_idx += 1
#             else:
#                 break
#     return cnt
#
#
# if __name__ == "__main__":
#     print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
#     print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5], 7))  # 6
#
#
# 계산한 리스트 따로 만듬
# 정렬된 리스트에서 혼합된 스코빌보다 아직 사용안된 두 스코빌이 작아도 새로운 두 스코빌의 혼합은 최소 이전 혼합 스코빌보다 같거나 크다
# stack으로 사용하자 x 먼저 들어온것 이 더 작으니까 큐다. a<=b<=c<=d, 찾아보니 이게 힙같은데 확실히는 잘..
def solution(scoville, K):
    scoville.sort()
    # 용량 초과된다. cq로 변환
    n = len(scoville) + 1
    mixed_scoville = [0] * n
    front = rear = 0

    # 스코빌도 q로 보자. front == idx
    idx = 0
    cnt = 0
    while True:
        if idx < len(scoville):
            # 함수로 만들자..
            if front != rear:
                if mixed_scoville[(front + 1) % n] < scoville[idx]:
                    a = mixed_scoville[(front + 1) % n]
                    front = (front + 1) % n
                else:
                    a = scoville[idx]
                    idx += 1

                # 두 번째 검사
                if idx < len(scoville):
                    if front != rear:  # 1
                        if mixed_scoville[(front + 1) % n] < scoville[idx]:
                            b = mixed_scoville[(front + 1) % n]
                            front = (front + 1) % n
                        else:
                            b = scoville[idx]
                            idx += 1
                    else:
                        b = scoville[idx]
                        idx += 1
                # 위 1번 조건문으로 b는 무조건 있다.
                else:
                    b = mixed_scoville[(front + 1) % n]
                    front = (front + 1) % n
            else:
                a = scoville[idx]
                idx += 1
                b = scoville[idx]
                idx += 1
        else:
            # 최소 1개는 있으므로 이때는 검사 안해도 된다.
            a = mixed_scoville[(front + 1) % n]
            front = (front + 1) % n
            if front != rear:
                b = mixed_scoville[(front + 1) % n]
                front = (front + 1) % n
            # 하나 남았다는 뜻이다.
            else:
                if a < K:
                    return -1
                else:
                    return cnt

        if a >= K:
            return cnt
        new_scoville = a + 2 * b
        cnt += 1

        rear = (rear + 1) % n
        mixed_scoville[rear] = new_scoville


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
    print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5], 7))  # 6
    print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5], 120))  # -1


# heap?
def heap_function(cq, cf, cr, q, f, r):
    n = len(cq)
    # cq is circular queue
    # 선형 큐가 검사의 우선순위를 갖는다? 둘 다 원형큐여도 되는데 그건 아직..
    if f + 1 != r:
        # cq is empty?
        if cf != cr:
            if cq[(cf + 1) % n] < q[f + 1]:
                a = cq[(cf + 1) % n]
                cf = (cf + 1) % n
            else:
                a = q[f + 1]
                f += 1
        else:
            a = q[f + 1]
            f += 1
    else:
        if cq != cr:
            a = cq[(cf + 1) % n]
            cf = (cf + 1) % n
        else:
            raise IndexError
    return a, cf, f


def solution(scoville, K):
    scoville.sort()
    # front
    idx = -1
    # rear
    n = len(scoville)
    # mixed scoville
    cq = [0] * n
    front = rear = 0

    cnt = 0
    while True:
        a, front, idx = heap_function(cq, front, rear, scoville, idx, n)
        if a >= K:
            return cnt
        if idx == n - 1 and front == rear:
            return -1
        b, front, idx = heap_function(cq, front, rear, scoville, idx, n)

        new_scoville = a + 2*b
        cnt += 1

        rear = (rear + 1) % n
        cq[rear] = new_scoville


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
    print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5], 7))  # 6
    print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5], 120))  # -1


