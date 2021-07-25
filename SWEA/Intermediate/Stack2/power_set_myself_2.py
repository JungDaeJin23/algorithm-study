# n개의 원소가 들어있는 집합의 2 ** n 개의 부분집합을 만들 때, True or False 값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법
def power_set(arr, sub, i=0):
    global ans
    if i == len(arr):
        tmp = ''
        for idx in range(len(arr)):
            if sub[idx]:
                tmp += str(arr[idx])
        ans.append(tmp)
    else:
        sub[i] = True
        power_set(arr, sub, i=i+1)
        sub[i] = False
        power_set(arr, sub, i=i + 1)


arr1 = [i for i in range(1, 5)]
sub1 = [False] * len(arr1)
ans = []
power_set(arr1, sub1)

ans.sort(key=lambda x: len(x))
print(*ans, sep='\n')