# N의 길이는 800자리를 넘지 않는다. 10^800..?
# the number of squares from 1 to 9 has a number of digits like [1 ,4 ,9, 6, 5, 6, 9, 4, 1] + [0]
# so all squared numbers are summation of that list
# (a*10 + b) **2 = a^2 * 10^2 + 2 아닌듯..
# possible_number = {'1': [1, 9], '4': [2, 8], '9': [3, 7], '6': [4, 6], '5': [5], '0': [0]}
# 앞자리 부터..? [1, 4, 9, 16, 25, 36, 49, 64, 81]
# possible_number = {'1': [1, 4], '4': [2, 7], '9': [3], '2': [5], '3': [6], '6': [8], '8': [9]}


# 뭐지..
N_str = input()
answer = 0

