N = int(input())
info_list = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    info_list.append((age, name))


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


info_list = bubble_sort(info_list)
for el in info_list:
    print(*el)