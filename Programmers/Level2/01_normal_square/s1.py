# Analyze a problem
# 왜 최대 공약수 인가
# 꼭지점에서 출발한 대각선이 사각형을 지나면서 최초로 꼭지점에 도달하는 위치를 보면 너비와 높이에서 최대 공약수로 나눠준 값이다.
# 위와 같은 최소 구조가 최대 공약수의 갯수 만큼 반복되기 때문에 최소 단위에서 사라지는 사각형의 갯수를 구한 다음에 최대 공약수로 곱해주면
# 총 손실되는 사각형의 갯수를 구할 수 있다.

# 그렇다면 어떻게 최소 구조에서의 손실되는 사각형의 갯수를 구할 것인가?
# 일단 한 변의 길이에 만큼 손실이 발생한다.
# 기울기를 살펴보면 h/w 이다. x는 0 부터 w 까지다. 그리고 [hx/w]의 x가 증가할 때마다 1 + ([hx/w] - [h(x-1)/w]) 개의 손실이 발생한다.
# 1은 기본적으로 발생하는 손실이다.
# [hx/w], hx/w = int + float 따라서 [hx/w] = int, [h(x-1)/w] = [hx/w - h/w] = [int + float - int' - float']
# float > float' 최대 공약수로 나누어 주었으므로 그렇다. 엄밀히는 잘 모르겠다.
# 따라서 int - int' 이것도 점화식으로 하면
# (h - a) + (a - a') + (a' - a'') + ... + (a[1] - 0) = h (w번째가 h이다.)
# 이러한 경우가 w 개 있으므로 w를 곱해주면 총 손실은 1 * w +, x는 1 부터 w까지의 합([hx/w] - [h(x-1)/w]) = w + h 이다.
# 여기서 엣지 케이스인 x가 w인 경우는 [hw/w] - [h(w-1)/w] = int - [int + float - int' - float']
# 원래라면 float가 float' 보다 크지만 여기서는 0이므로 int - (int - int' -1)  = int' + 1
# 여태가지는 int - (int - int')로 int' 만큼의 양에 기본적인 손실 양 1을 따로 더해주었지만  blabla
# 마지막에 값 중복했으므로 -1 해준다.
# W + H - gcd(W,H) = gcd(W, H)(w + h - 1)



def my_gcd(m, n):
    if n > m:
        m, n = n, m
    while n:
        m, n = n, m % n
    return m


def solution(w, h):
    d = my_gcd(w, h)
    if w < h:
        numerator, denominator = w, h
    else:
        numerator, denominator = h, w

    return w * h - (denominator + (numerator // d - 1) * d)
# def solution(w, h):
#     """
#     w = width
#     h = height
#     """
#     # 1-1. find prime number under lower number
#     # 1-2. find all factor if lower numer
#     # 1-3.

#     # 2-1. just repeat diviation by all number under lower number
#     if w > h:
#         denominator, numerator = w, h
#     else:
#         denominator, numerator = h, w
#     original_denominator = denominator
#     cycle = 1
#     for num in range(2, numerator + 1):
#         while (not numerator % num) and (not denominator % num):
#             cycle *= num
#             numerator //= num
#             denominator //= num
#         if num > numerator:
#             break

#     return w * h - (original_denominator + (numerator - 1) * cycle)