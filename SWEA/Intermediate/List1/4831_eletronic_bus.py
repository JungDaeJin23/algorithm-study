T = int(input())

for tc in range(1, T+1):
    # 한번 충전으로 최대한 이동할 수 있는 정류장 수 K,
    # 종점인 N번 정류장,
    # 충전기가 설치된 M개의 정류장 번호
    K, N, M = map(int, input().split())
    electric_stations = list(map(int, input().split()))
    charging_cnt = 0
    position = 0
    # queue 사용 그러나 정류장만 탐색한다.
    passed_station = 0
    station_idx = 0
    while station_idx < len(electric_stations):
        if position + K >= N:
            break

        if electric_stations[station_idx] - position > K:
            if passed_station:
                position = passed_station
                passed_station = 0
                charging_cnt += 1
            else:
                charging_cnt = 0
                break
            continue
        elif electric_stations[station_idx] - position == K:
            charging_cnt += 1
            position = electric_stations[station_idx]
            passed_station = 0

        else:  # electric_stations[station_idx] - position < K:
            passed_station = electric_stations[station_idx]

        station_idx += 1
    else:
        if passed_station:
            position = passed_station

        if position + K >= N:
            charging_cnt += 1
        else:
            charging_cnt = 0

    print('#{0} {1}'.format(tc, charging_cnt))

# # Queue를 사용해서 가장 낮중에 들어간 정류장을 가져온다.
# queue = [0]*M
# front = rear = -1
#
# position = 0
# left_energy = K
# electric_station_idx = 0
# charging_cnt = 0
# # 도착 못하는 경우는 있다. There are no cases bus cant reach(arrive) the destination.
# # loop K times. not necessary
# while position < N:
#     position += 1
#     left_energy -= 1
#     if left_energy == 0:
#         charging_cnt += 1
#
#     if electric_stations[electric_station_idx] == position:
#         queue[rear+1] = electric_station_idx
#         rear += 1
#         electric_station_idx += 1
#
