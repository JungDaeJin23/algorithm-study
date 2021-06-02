T = int(input())

# greedy: 항상 갈 수 있는 최대 거리의 정류장을 선택한다.
for tc in range(1, T+1):
    # 한번 충전으로 최대한 이동할 수 있는 정류장 수 K,
    # 종점인 N번 정류장,
    # 충전기가 설치된 M개의 정류장 번호
    K, N, M = map(int, input().split())
    electric_stations = list(map(int, input().split()))
    charging_cnt = 0
    position = 0
    passed_station = 0

    station_idx = 0
    while station_idx < len(electric_stations):
        if position + K >= N:
            break

        # 현재 위치에서 도달 못하는 충전소 만남
        if electric_stations[station_idx] - position > K:
            # 갈 수 있는 정류장에서 가장 먼 정류장에 들렸다.
            if passed_station:
                position = passed_station
                passed_station = 0
                charging_cnt += 1
            # 그럼에도 가지 못한다. 도달 불가
            else:
                charging_cnt = 0
                break
            continue
        # 최대 거리에 정류장이 있다. 무조건 들른다.
        elif electric_stations[station_idx] - position == K:
            charging_cnt += 1
            position = electric_stations[station_idx]
            passed_station = 0
        # 정류장을 만났지만 아직 연료에 여유가 있다. 기억만 한다.
        else:  # electric_stations[station_idx] - position < K:
            passed_station = electric_stations[station_idx]

        station_idx += 1
    # break로 loop 탈출 시에는 실행되지 않는다.
    # while내에서 마지막 정류소를 매번 확인 하는 것보다 while else 활용
    else:
        if passed_station:
            position = passed_station
            charging_cnt += 1

        if position + K < N:
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
