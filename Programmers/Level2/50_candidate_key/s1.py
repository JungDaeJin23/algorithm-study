# 부분집한(조합) 문제 최대 2^8 -1
# column major search
# DP -> 열 별로 primekey(index)사용해서 [dict0,dict1] 저장해서 사용?


def my_combi(used, i=0, a=[]):
    for idx in range(i, len(used)):
        if not used[idx]:
            used[idx] = True
            my_combi(used, idx, a)

    return a
def solution1(relation):
    col_dict_list = [dict() for _ in range(len(relation[0]))]
    used = [True] * len(relation[0])
    # O(N) 데이터가 N by N으로 들어와서 N^2 같지만 N이 맞다고 생각한다.
    for j in range(len(relation[0])):
        for i in range(len(relation)):
            if col_dict_list[j].get(relation[i][j]):
                # append의 big O 는 O(1)..?
                col_dict_list[j].get(relation[i][j]).append(i)
                used[j] = False
            else:
                col_dict_list[j][relation[i][j]] = [i]
    answer = sum(used)

    return answer


# def solution(relation):
#     col_dict_list = [dict() for _ in range(len(relation[0]))]
#     used = [True] * len(relation[0])
#     # O(N) 데이터가 N by N으로 들어와서 N^2 같지만 N이 맞다고 생각한다.
#     for j in range(len(relation[0])):
#         for i in range(len(relation)):
#             if col_dict_list[j].get(relation[i][j]):
#                 # append의 big O 는 O(1)..?
#                 col_dict_list[j].get(relation[i][j]).append(i)
#                 used[j] = False
#             else:
#                 col_dict_list[j][relation[i][j]] = [i]
#
#     answer = sum(used)
#     temp = [[] for _ in range(len(relation[0]))]
#     for i in range(len(col_dict_list)):
#         if not used[i]:
#             for key, value in col_dict_list[i].items():
#                 if len(value) > 1:
#                     temp[i].append(value)
#
#     def my_perm(i, a, j=0):
#         if not i:
#             return
#         for idx in range(j, len(used)):
#             if not used[idx]:
#                 used[idx] = True
#                 my_perm(i-1, a, idx)
#                 used[idx] = False
#
#     def count_possible_cases(i):
#         a = []
#         my_perm(i, a)
#         print(a)
#         return 0
#
#     # print(temp)
#     left_record = len(used) - sum(used)
#     tmp = 2
#     if left_record < tmp:
#         return answer
#     a = count_possible_cases(tmp)
#
#     while True:
#         answer += a
#         left_record = len(used) - sum(used)
#         tmp += 1
#         if left_record < tmp:
#             return answer
#         a = count_possible_cases(tmp)


if __name__ == "__main__":
    print(solution1([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
    print(solution1([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
