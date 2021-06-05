# Brute force
def find_pattern(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    i = 0
    j = 0
    while i < n1 and j < n2:
        if str1[i] != str2[j]:
            j -= i
            i = -1

        i += 1
        j += 1

    if i == n1:
        return 1
    return 0


# input and output
T = int(input())
for tc in range(1, T + 1):
    S1 = input()
    S2 = input()
    print("#{0} {1}".format(tc, find_pattern(S1, S2)))
