# heapify 기능 구현
# scoville의 길이는 2 이상 1,000,000 이하 약 2^20


def heappush(heap, heap_count, el):
    heap_count += 1
    heap[heap_count] = el
    child = heap_count
    parent = child // 2
    while parent:
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2
        else:
            break
    return heap, heap_count


def heappop(heap, heap_count):
    return_value, heap[1] = heap[1], heap[heap_count]
    heap_count -= 1
    parent = 1
    ch1 = parent * 2
    ch2 = parent * 2 + 1
    while ch1 <= heap_count:
        if ch2 <= heap_count:
            ch = ch1 if heap[ch1] < heap[ch2] else ch2
        else:
            ch = ch1

        if heap[parent] > heap[ch]:
            heap[parent], heap[ch] = heap[ch], heap[parent]
            parent = ch
            ch1 = parent * 2
            ch2 = parent * 2 + 1
        else:
            break
    return return_value, heap, heap_count


def my_heapify(iterable):
    heap_count = 0
    heap = [0]*(len(iterable) + 1)
    for el in iterable:
        heap_count += 1
        heap[heap_count] = el
        child = heap_count
        parent = child//2
        while parent:
            if heap[parent] > heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
                parent = child//2
            else:
                break
    return heap, heap_count


def solution(scoville, K):
    heap_scoville, heap_count = my_heapify(scoville)
    cnt = 0
    # 뒤로는 다 정렬 되어 있는데 꼭 맨 마지막 값을 앞으로 가져와서 정렬해야 될까?
    while heap_count:
        smallest_scoville, heap_scoville, heap_count = heappop(heap_scoville, heap_count)
        if smallest_scoville >= K:
            return cnt
        # second_smaller_scoville, heap_scoville, heap_count = heappop(heap_scoville, heap_count)
        second_smaller_scoville = heap_scoville[1]
        new_scoville = smallest_scoville + second_smaller_scoville*2
        cnt += 1
        # heap_scoville, heap_count = heappush(heap_scoville, heap_count, new_scoville)
        heap_scoville[1] = new_scoville
        parent = 1
        ch1 = parent * 2
        ch2 = parent * 2 + 1
        while ch1 <= heap_count:
            if ch2 <= heap_count:
                ch = ch1 if heap_scoville[ch1] < heap_scoville[ch2] else ch2
            else:
                ch = ch1

            if heap_scoville[parent] > heap_scoville[ch]:
                heap_scoville[parent], heap_scoville[ch] = heap_scoville[ch], heap_scoville[parent]
                parent = ch
                ch1 = parent * 2
                ch2 = parent * 2 + 1
            else:
                break
    return -1
