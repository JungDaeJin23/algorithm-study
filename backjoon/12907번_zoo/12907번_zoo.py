# cases of combination?
# 동물원에 동물이 N마리 있고 모든 동물의 키는 다 다르다.
# 동물의 수 N (1 ≤ N ≤ 40)
# brute force? check every case 2^40
# first step sort
# stack if next coming element breaks the rule, return 0
# rule push the element if element's value is same top
# 토끼와 고양이 두 집단의 교환 가능한 경우는 더 작은 집단의 2 ** (top + 2) 크기가 같으면 2 ** (top + 1)


N = int(input())
count_of_exceeding_own_height = sorted(list(map(int, input().split())))

stack1 = [0] * 41
stack2 = [0] * 41
top1 = top2 = -1

for count in count_of_exceeding_own_height:
    if count == top1 + 1:
        top1 += 1
        # stack1[top1] = count
    elif count == top2 + 1:
        top2 += 1
        # stack2[top2] = count
    else:
        print(0)
        break
else:
    if top1 != top2:
        print(2**(top2 + 2))
    else:
        print(2**(top2 + 1))

