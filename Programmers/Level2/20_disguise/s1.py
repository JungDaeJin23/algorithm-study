#  매일 다른 옷을 조합 combine different clothes every day
# 2차원 배열 clothes
#  each row has [의상의 이름, 의상의 종류]
# there are no same clothes
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 조합, 종류:n nC1 + ... + nCn = 2^n - 1
# 같은 종류에 있는 옷을 어떻게 계산에 넣어야 될까?
# 조합 or 부분집합 구하는 로직에서 해당 원소가 포함되면 +1 * len(element1) * len(element2)


def my_combi(dictionary, categories, idx=0, result=1, total=0):
    while idx < len(categories):
        # 이번에 포함된 원소가 가질수 있는 경우의 수
        cnt = len(dictionary[categories[idx]])
        # 이전에 포함되어 있던 것들의 경우의 수 * 이번에 추가된 것의 경우의 수
        # result *= cnt
        # 이번 조합이 가지는 경우의 수 더해주기
        total += result * cnt
        # 이전에 포함되어 있던 것들의 경우의 수 더하기
        total += my_combi(dictionary, categories, idx + 1, result * cnt)
        # result = 1  # == result // cnt
        idx += 1

    return total


def solution(clothes):
    # make clothes dictionary (category, clothe)
    clothes_dict = {}
    for clothe in clothes:
        name, category = clothe
        if clothes_dict.get(category):
            clothes_dict[category].append(name)
        else:
            clothes_dict[category] = [name]

    # 경우의 수
    answer = 1
    for val in clothes_dict.values():
        answer *= (len(val) + 1)
    answer -= 1
    # combination
    # answer = my_combi(clothes_dict, list(clothes_dict.keys()))
    return answer


if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"],
                    ["crowmask", "face1"], ["bluesunglasses", "face1"], ["smoky_makeup", "face1"],
                    ["crowmask", "face12"], ["bluesunglasses", "face12"], ["smoky_makeup", "face12"]]))