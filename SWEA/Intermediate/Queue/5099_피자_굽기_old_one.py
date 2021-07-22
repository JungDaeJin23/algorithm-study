def bake_pizza(capacity_of_oven, waiting_pizza_list):
    baked_pizza_list = []
    oven = [(i + 1, waiting_pizza_list.pop(0)) for i in range(capacity_of_oven)]
    pizza_number = capacity_of_oven + 1
    cnt_of_pizza_in_oven = capacity_of_oven
    entrance = 0

    while cnt_of_pizza_in_oven:
        pizza_num = oven[entrance][0]
        cheese = oven[entrance][1]//2
        if pizza_num !=0 and cheese == 0:
            cnt_of_pizza_in_oven -= 1
            baked_pizza_list.append(pizza_num)
            if waiting_pizza_list:
                oven[entrance] = (pizza_number, waiting_pizza_list.pop(0))
                pizza_number += 1
                cnt_of_pizza_in_oven += 1
            else:
                oven[entrance] = (0, 0)
        else:
            oven[entrance] = (pizza_num, cheese)
        entrance = (entrance + 1) % capacity_of_oven
    return baked_pizza_list[-1]


# input and output
T = int(input())
for tc in range(1, T + 1):
    # N: 화덕의 크기, M: 피자 개수m Ci: 피자에 뿌려진 치즈의 양
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    print("#{0} {1}".format(tc, bake_pizza(N, Ci)))
