def solution(name):
    # 모든 알파벳이 A가 아니라면 각각 A와의 ord 차이를 구해서 더하면 됨(1~13)
    # A~Z가 25번 (26-1번), 그니까 13 N은 >> 방향 O부터는 << 방향
    # 처음에는 좌우 방향을 처음 한번만 정하고 쭉 유지하는 줄 알았는데 아니었다
    # BBAAAAAC 같은 경우 0번 (오른쪽 1번 이동 > ) 1번 (왼쪽 2번 이동 << ) -1번
    # 이런식으로 이동방향을 바꾼다. 현 위치에서 좌우 중에서 0이 아닌 값이 있는 가까운 곳으로 이동
    rename = [(26 - (ord(n) - ord('A'))) if (ord(n) - ord('A')) > 13 else (ord(n) - ord('A')) for n in name]

    result = 0
    # 0번 인덱스부터 변경 시작
    idx = 0

    # 모두 변경 완료되기 전까지 반복
    while rename != [0] * len(name):
        # 조이스틱 상or하 누른만큼('A'와의 거리만큼) 결과에 더한다
        result += rename[idx]
        # 변경완료했으니 0으로 만들어준다
        rename[idx] = 0

        # 다 바뀌었다면 종료
        if rename == [0] * len(name):
            return result

        # 현재 위치에서 좌우로 0이 아닌 값(바꿔야할 값)이 나올때까지 가본다
        r, l = (1, 1)
        while rename[idx + r] == 0:
            r += 1

        while rename[idx - l] == 0:
            l += 1

        # 왼쪽이 더 가깝다면, 왼쪽으로 간다
        if l < r:
            # 이동한만큼 조이스틱을 <로 움직인거니까 그만큼 결과에 더한다
            result += l
            idx -= l
        # 반대
        else:
            result += r
            idx += r

    return result


if __name__ == "__main__":
    print(solution("BZBA"))  # 5
    print(solution("AAAABAA"))  # 4
    print(solution("BBAAAB"))  # 6
    print(solution("ABABBAAAAAABAAAB"))  # 18
    print(solution("ABABAAAB"))  # 8