# 문제 주소
# https://programmers.co.kr/learn/courses/30/lessons/12913

# 문제 접근 방법 approach
# 1. brute force
# 2. greedy -> 각 행의 최대와 두 번째로 큰 값을 구하고 다음 행과의 관계와 합을 살펴본다.(wrong)
# 3. DP 규칙에 맞게 누적합을 구한다.
# 부분합의 최대가 전체합의 최대를 보장하지 않는다.
# [[3, 5],
#  [7, 8],
#  [6, 4]]


# 코드
# 1. brute force
# def solution(land):
# #     answer = 0
# #     for row in land:
# #         # 100 이하의 자연수
# #         largest = 0  # largest = row[0]
# #         second_large = 0  # second_large = row[0]
# #         for col, num in enumerate(row):
# #             if largest == 0:
# #                 pass
# #
# #     return answer


# 3. DP 다음행에 같은 열 원소 사용 불가 조건은 가장 큰 값과 두번째로 큰 값을 보면 해결된다.
def solution(land):
    for row in range(len(land)-1):  # 마지막 행 제외
        max_col = 0
        second_max_col = 0
        for col in range(len(land[row])):
            if land[row][col] > land[row][max_col]:
                max_col = col
        for col in range(len(land[row])):
            if land[row][col] > land[row][second_max_col] and col != max_col:
                second_max_col = col

        # 다음 행에 값 누적시키기 같은 열은 두번째로 큰 값을 더해준다.
        for col in range(len(land[row+1])):
            if col == max_col:
                land[row+1][col] += land[row][second_max_col]
            else:
                land[row + 1][col] += land[row][max_col]
    return max(land[len(land)-1])

# 시간 복잡도

# 공간 복잡도?