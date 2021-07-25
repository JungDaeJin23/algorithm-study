def power_set(arr, sub, size, tmp=''):
    global ans
    if len(tmp) == size:
        ans.append(tmp)
        return
    for i in range(len(arr)):
        if not sub[i]:
            sub[i] = True
            power_set(arr, sub, size, tmp=tmp+str(arr[i]))
            sub[i] = False


arr1 = [i for i in range(1, 5)]
sub1 = [False] * len(arr1)
ans = []
power_set(arr1, sub1, len(arr1)-3)
# ans.sort(key=lambda x: len(x))
print(*ans, sep='\n')
print(len(ans))
