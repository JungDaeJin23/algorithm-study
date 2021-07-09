N = int(input())
info_list = []
# 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수
counting_list = [0]*201
for _ in range(N):
    age, name = input().split()
    age = int(age)
    counting_list[age] += 1
    info_list.append((age, name))
# accumulated_list
for idx in range(1, len(counting_list)-1):
    counting_list[idx+1] += counting_list[idx]

# stable sort
sorted_info_list = [0] * len(info_list)
for idx in range(len(info_list)-1, -1, -1):
    age, name = info_list[idx]
    counting_list[age] -= 1
    sorted_info_list[counting_list[age]] = (age, name)

for el in sorted_info_list:
    print(*el)