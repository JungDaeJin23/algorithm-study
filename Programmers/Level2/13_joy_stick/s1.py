# Greedy
# 왼쪽으로 이동하는 경우는 시작점 바로 오른쪽에 A가 있을 때이다. 그 외에는 어떻게 하던지 거쳐가게 되어있다.(가장 우측 제외)
# 아래로 돌리는 경우는 A를 제외하고 (26 - 1) / 2 = 12.5, M=13 기준으로 어느 방향으로 돌릴 지 정해진다. (M은 방향 상관 없음)
# 정방향 <= M, ord(x) - ord('A'); 역방향 > M, ord('Z') - ord(x) + 1
# BBAAAAABB 가운데 A가 돌아가는 길이보다 많이 분포할 경우 찍고 돌아와야 된다.

#
# # 마지막 경우 해결 못함
# def solution(name):
#     answer = 0
#     right_side_A_length = 0
#     idx = 1
#     while name[idx] == 'A':
#         right_side_A_length += 1
#         idx += 1
#     left_side_A_length = 0
#     idx = len(name) - 1
#     while name[idx] == 'A':
#         left_side_A_length += 1
#         idx -= 1
#     max_length = right_side_A_length if right_side_A_length > left_side_A_length else left_side_A_length
#     # 가운데 기준으로 A가 몇개 분포해 있는지 확인한다.
#     longest_A = 0
#     cnt = 0
#     for idx in range(1, len(name)):
#         if name[idx] == 'A':
#             cnt += 1
#         else:
#             if cnt > longest_A:
#                 longest_A = cnt
#             cnt = 0
#     # 마지막이 A일 경우
#     if cnt > longest_A:
#         longest_A = cnt
#     # 이름이 전부 'A'로 이루어진 경우 카운트 한다.
#     A_counter = 0
#     # 좌우 생각 안하고 오른쪽으로만
#     for alphabet in name:
#         if alphabet == 'A':
#             A_counter += 1
#
#         if ord(alphabet) > ord('M'):
#             answer += ord('Z') - ord(alphabet) + 1
#         else:
#             answer += ord(alphabet) - ord('A')
#         # move right count
#         answer += 1
#     # minus 마지막 칸에서 오른쪽으로 이동하는 횟수
#     answer -= 1
#     # 마지막 칸이 'A' 라면 마지막 칸으로 이동할 필요도 없으므로 감해준다.
#     # 굳이 왼쪽으로 가지말고 index 1번 자리가 1이면 왼쪽을 갔다고 치고 위와 같은 이유로 1을 빼준다.
#     # 그럴 경우 'AAAABAA' 4, 일 경우 문제가 생긴다. 시작점을 기준을 A가 덜 연속된 곳으로 가야된다.
#     # -1이 아닌 긴 쪽의 A의 길이를 빼주면 된다.
#
#     if alphabet == 'A' or name[1] == 'A':
#         answer -= max_length
#     if A_counter == len(name):
#         return 0
#
#     return answer
#
#
# if __name__== "__main__":
#     print(solution("BZBA")) # 5
#     print(solution("AAAABAA")) # 4
#     print(solution("BBAAAB")) # 6
#
#
# # 가장 긴 연속된 A를 하나로 합쳐서 계산?
# def solution(name):
#     answer = 0
#     # 위 아래 돌리는 횟수
#     for alphabet in name:
#         if ord(alphabet) > ord('M'):
#             answer += ord('Z') - ord(alphabet) + 1
#         else:
#             answer += ord(alphabet) - ord('A')
#
#     # 좌, 우 최적화...
#     right_side_A_length = 0
#     idx = 1
#     while name[idx] == 'A':
#         right_side_A_length += 1
#         idx += 1
#     left_side_A_length = 0
#     idx = len(name) - 1
#     while name[idx] == 'A':
#         left_side_A_length += 1
#         idx -= 1
#     max_length = right_side_A_length if right_side_A_length > left_side_A_length else left_side_A_length
#
#     answer += len(name) - max_length - 1
#
#     return answer
#
#
# if __name__== "__main__":
#     print(solution("BZBA")) # 5
#     print(solution("AAAABAA")) # 4
#     print(solution("BBAAAB")) # 6
#
# # 가장 긴 연속된 A를 하나로 합쳐서 계산?
# def solution(name):
#     answer = 0
#     # 가장 길게 연속된 A를 찾아서 idx 0 제외
#     longest_A = 0
#     cnt = 0
#     for idx in range(1, len(name)):
#         if name[idx] == 'A':
#             cnt += 1
#         else:
#             if cnt > longest_A:
#                 longest_A = cnt
#             cnt = 0
#     # 마지막이 A일 경우
#     if cnt > longest_A:
#         longest_A = cnt
#     # 위 아래
#     for alphabet in name:
#         if ord(alphabet) > ord('M'):
#             answer += ord('Z') - ord(alphabet) + 1
#         else:
#             answer += ord(alphabet) - ord('A')
#
#     # 좌, 우
#     answer += len(name) - longest_A
#     return answer
#
#
# if __name__== "__main__":
#     print(solution("BZBA")) # 5
#     print(solution("AAAABAA")) # 4
#     print(solution("BBAAAB")) # 6
#
#
# ####################################
# # AAA에서 네임으로 바꾸는 것이다 여태까지 이름을 AAA로 하고 있었다. 차이가 없을 지도 모르지만 다시
# # 삼성시 버스 문제..?
# # 그리드로 다시 해보자.. 가운데서 돌리고 양쪽 보고 동시에 나아가자
#
# def solution(name):
#     answer = 0
#     # 위 아래
#     for alphabet in name:
#         if ord(alphabet) > ord('M'):
#             answer += ord('Z') - ord(alphabet) + 1
#         else:
#             answer += ord(alphabet) - ord('A')
#
#     cnt_list = []
#     a_cnt = 0
#     cnt = 0
#     for alphabet in name[1:]:
#         if alphabet == 'A':
#             if cnt:
#                 cnt_list.append(cnt)
#             cnt = 0
#             a_cnt += 1
#         else:
#             if a_cnt:
#                 cnt_list.append(str(a_cnt))
#             a_cnt = 0
#             cnt += 1
#     if cnt:
#         cnt_list.append(cnt)
#     if a_cnt:
#         cnt_list.append(str(a_cnt))
    # print(cnt_list, answer)
    # 1. 가장 긴 A의 양옆에 숫자가 있고
    # 끝에서 부터 A를 포함한 모든 수를 더한 것 중에 작은 수를 * 2 하고 A의 길이와 비교한다.
    # 더 작은쪽과 나머지를 더한ㄹㅈㅁㄷㄹㅈㅁㄷ롬ㅈ로

# if __name__== "__main__":
#     print(solution("BZBA")) # 5
#     print(solution("AAAABAA")) # 4
#     print(solution("BBAAAB")) # 6


def solution(name):
    answer = 0
    # 위 아래
    for alphabet in name:
        if ord(alphabet) > ord('M'):
            answer += ord('Z') - ord(alphabet) + 1
        else:
            answer += ord(alphabet) - ord('A')
    reversed_name = name[0]
    for idx in range(len(name) - 1, 0, -1):
        reversed_name += name[idx]
    # print(reversed_name)
    common_A = 0

    # 뒤에 붙은 A 제거
    i = len(name) - 1
    while 0 <= i and name[i] == 'A':
        i -= 1
    name = name[:i + 1]

    i = len(reversed_name) - 1
    while 0 <= i and reversed_name[i] == 'A':
        i -= 1
    reversed_name = reversed_name[:i + 1]
    short_case = len(name) if len(name) < len(reversed_name) else len(reversed_name)

    longest_A = 0
    cnt = 0
    l_end_idx = -1
    for idx in range(1, len(name)):
        if name[idx] == 'A':
            cnt += 1
        else:
            if cnt > longest_A:
                l_end_idx = idx
                longest_A = cnt
            cnt = 0
    # 마지막이 A일 경우
    if cnt > longest_A:
        l_end_idx = idx
        longest_A = cnt
    # print(l_end_idx - longest_A, l_end_idx - 1)
    if (l_end_idx - longest_A - 1) < (len(name) - l_end_idx):
        small_center = (l_end_idx - longest_A - 1) * 2 + (len(name) - l_end_idx)
    else:
        small_center = (len(name) - l_end_idx) * 2 + (l_end_idx - longest_A - 1)
    # print(small_center, short_case - 1)
    if l_end_idx > 0 and l_end_idx - longest_A != 1 and l_end_idx - 1 != len(name) - 1:
        if small_center < short_case:
            short_case = small_center + 1
    answer += short_case - 1

    return answer


if __name__ == "__main__":
    print(solution("BZBA"))  # 5
    print(solution("AAAABAA"))  # 4
    print(solution("BBAAAB"))  # 6
    print(solution("ABABBAAAAAABAAAB"))  # 18
    print(solution("ABABAAAB"))  # 8