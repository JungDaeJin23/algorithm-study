
# input data
T = int(input())
info_list = list()
charge_stop_list = list()
for test_case in range(T):
    # K, N, M = map(int, input().split())
    info_list.append(list(map(int, input().split())))
    charge_stop_list.append(list(map(int, input().split())))


def is_arrived(k, n, m, recharge_list):
    """
    :param reload_list: 충전기가 설치된 M개의 정류장 번호 리스트
    :param k: 한번 충전으로 최대한 이동할 수 있는 정류장 수
    :param n: 종점인 N번 정류장
    :param m:충전기가 설치된 M개의 정류장
    :return:
    """
    bus_stop = [0] * (n + 1)
    for idx in recharge_list:
        bus_stop[idx] = 1
    bus_position = k
    cnt = 0
    while bus_position < n:
        for _ in range(k):
            if bus_stop[bus_position]:
                cnt += 1
                break
            else:
                bus_position -= 1
        else:
            return  0
        bus_position += k
    return cnt


# output
for i in range(T):
    print("#{0} {1}".format(i+1, is_arrived(info_list[i][0], info_list[i][1], info_list[i][2], charge_stop_list[i])))