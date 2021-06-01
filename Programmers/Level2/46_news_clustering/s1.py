def J(A, B):
    if len(A) == 0 and len(B) == 0 or A == B:
        return 1
    a = b = 0
    common_cnt = 0
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            common_cnt += 1
            a += 1
            b += 1
        elif A[a] > B[b]:
            b += 1
        else:
            a += 1

    return common_cnt/(len(A) + len(B) - common_cnt)

def solution(str1: str, str2: str):

    A = sorted([str1[i].lower() + str1[i+1].lower() for i in range(len(str1)-1) if (str1[i].isalpha() and str1[i+1].isalpha())])
    B = sorted([str2[i].lower() + str2[i+1].lower() for i in range(len(str2) - 1) if (str2[i].isalpha() and str2[i + 1].isalpha())])
    # print(A, B)
    answer = J(A, B)
    return int(answer * 65536)


if __name__ == "__main__":
    print(solution("FRANCE",	"french"))
    print(solution("E=M*C^2",	"e=m*c^2"))
    print(solution("handshake", "shake hands"))  # 65536
