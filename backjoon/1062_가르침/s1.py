# 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다
# 1 4
# antatica
N, K = map(int, input().split())
alphabet = [0]*26
candidate_alphabet = set()
words = []
unknown_alphabet_in_words = []
# 최소 요구치
alphabet[ord('a')-ord('a')] = 1
alphabet[ord('n')-ord('a')] = 1
alphabet[ord('t')-ord('a')] = 1
alphabet[ord('i')-ord('a')] = 1
alphabet[ord('c')-ord('a')] = 1
K -= 5
ans = 0
max_ = 0
if K > 0:
    for _ in range(N):
        word = input()
        tmp = set()
        for alpha in word:
            if alphabet[ord(alpha)-ord('a')] == 0:
                tmp.add(alpha)
        if tmp:
            if len(tmp) <= K:
                for alpha in tmp:
                    candidate_alphabet.add(alpha)
                words.append(tmp)
        else:
            ans += 1

# 단순히 가장 많이 중복되는 알파벳을 배우면 안된다.
# brute force?
# 후보군에 등장하는 알파뱃의 갯수 C K 개를 모조리 탐색한다.
    from itertools import combinations

    for comb in combinations(candidate_alphabet, K):
        cnt = 0
        tmp = set(comb)
        for word in words:
            if not (word - tmp):
                cnt += 1
        if cnt > max_:
            max_ = cnt
print(ans+max_)