# 부분합 개념 사용
# make a trucks passing throught a bridge as linear queue X circular queue


def solution(bridge_length, weight, truck_weights):
    bridge_cq = [0] * (bridge_length + 1)
    n = len(bridge_cq)
    front = 0
    rear = n - 1
    weight_on_bridge = 0
    time = 0
    idx = 0

    time += 1
    weight_on_bridge -= bridge_cq[(front + 1) % n]
    bridge_cq[(front + 1) % n] = 0
    front = (front + 1) % n
    if idx < len(truck_weights) and weight_on_bridge + truck_weights[idx] <= weight:
        rear = (rear + 1) % n
        bridge_cq[rear] = truck_weights[idx]
        weight_on_bridge += truck_weights[idx]
        idx += 1
    else:
        rear = (rear + 1) % n

    while weight_on_bridge:
        time += 1
        weight_on_bridge -= bridge_cq[(front + 1) % n]
        bridge_cq[(front + 1) % n] = 0
        front = (front + 1) % n
        if idx < len(truck_weights) and weight_on_bridge + truck_weights[idx] <= weight:
            rear = (rear + 1) % n
            bridge_cq[rear] = truck_weights[idx]
            weight_on_bridge += truck_weights[idx]
            idx += 1
        else:
            rear = (rear + 1) % n

    return time


########################################################
# solved in the past;              solved in past time
# def solution(bridge_length, weight, truck_weights):
#     total_elapsed_time = 0
#     first_time_trucks_num = len(truck_weights)
#     bridge_queue_list = [0 for _ in range(bridge_length)]
#     arrived_trucks_list = []
#
#     while first_time_trucks_num != len(arrived_trucks_list):
#         next_truck_weight = truck_weights[0] if truck_weights else 0
#         arrived_truck = bridge_queue_list.pop(0)
#
#         if arrived_truck:
#             arrived_trucks_list.append(arrived_truck)
#
#         if sum(bridge_queue_list) + next_truck_weight <= weight:
#             depart_truck = truck_weights.pop(0) if truck_weights else 0
#             bridge_queue_list.append(depart_truck)
#         else:
#             for idx in range(len(bridge_queue_list)):
#                 if bridge_queue_list[idx]:
#                     break
#             if idx:
#                 bridge_queue_list = bridge_queue_list[idx:] + bridge_queue_list[:idx] + [0]
#                 total_elapsed_time += idx
#             else:
#                 bridge_queue_list.append(0)
#             # bridge_queue_list.append(0)
#
#         total_elapsed_time += 1
#
#     return total_elapsed_time

if __name__ =="__main__":
    print(solution(2, 10, [7,4,5,6]))  # 8
