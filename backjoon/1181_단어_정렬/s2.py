# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
N = int(input())
words = [input() for _ in range(N)]


def is_word1_forward_than_word2(word1, word2):
    if len(word1) < len(word2):
        return True
    elif len(word1) > len(word2):
        return False

    for idx in range(len(word1)):
        if ord(word1[idx]) < ord(word2[idx]):
            return True
        elif ord(word1[idx]) > ord(word2[idx]):
            return False


def merge_sort(arr, start, end):
    if end - start <= 1:
        if end == start:
            return [arr[start]]
        if arr[start] == arr[end]:
            return [arr[start]]
        if is_word1_forward_than_word2(arr[start], arr[end]):
            return [arr[start], arr[end]]
        return [arr[end], arr[start]]
    middle = (start + end) // 2
    left_arr = merge_sort(arr, start, middle)
    right_arr = merge_sort(arr, middle + 1, end)
    left_idx = 0
    right_idx = 0
    new_arr = []
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] == right_arr[right_idx]:
            new_arr.append(left_arr[left_idx])
            left_idx += 1
            right_idx += 1
        else:
            if is_word1_forward_than_word2(left_arr[left_idx], right_arr[right_idx]):
                new_arr.append(left_arr[left_idx])
                left_idx += 1
            else:
                new_arr.append(right_arr[right_idx])
                right_idx += 1
    new_arr.extend(left_arr[left_idx:])
    new_arr.extend(right_arr[right_idx:])
    return new_arr


sorted_words = merge_sort(words, 0, len(words)-1)
print(*sorted_words, sep='\n')