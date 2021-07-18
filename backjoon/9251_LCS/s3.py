str1 = input()
str2 = input()
if len(str1) < len(str2):
    shorter_one = str1
    longer_one = str2
else:
    shorter_one = str2
    longer_one = str1


used = [0]*len(shorter_one)
duplicated_check_dict = dict()
for i in range(len(shorter_one)):
    if duplicated_check_dict.get(shorter_one[i]):
        used[i] = 1
    else:
        duplicated_check_dict[shorter_one[i]] = 1
# position_dict = dict()
# for i in range(len(shorter_one)):
#     if position_dict.get(shorter_one[i]):
#         position_dict[shorter_one[i]].append(i)
#     else:
#         position_dict[shorter_one[i]] = [i]

idx = 0
stack = []
while idx < len(longer_one):
    for jdx in range(len(shorter_one)):
        if used[jdx]:
            continue
        if shorter_one[jdx] == longer_one[idx]:
            used[jdx] = 1
            stack.append((jdx, 1))
    for i in range(len(stack)):
        index, cnt = stack[i]
        for jdx in range(index+1, len(shorter_one)):
            if longer_one[idx] == shorter_one[jdx]:
                cnt += 1
                index = jdx
                break
        stack[i] = (index, cnt)
    idx += 1

stack.sort(key=lambda x: x[1], reverse=True)
print(stack[0][1])