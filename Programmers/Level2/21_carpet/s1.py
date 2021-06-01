# 넓이 = 밑변 * 높이
# 둘레 = (밑변 + 높이) * 2 - 4 (모서리를 공유한다는 조건이 붙는다.)
# 둘레 = brown, 넓이 = brown + yellow
# 밑변 >= 높이
# 밑변: W, 높이: H -> b + y = W * H, b = 2*(W + H) - 4
# H = (b + y)/W -> b = 2*((b + y)/W + W) - 4
# 2W^2 -(4 + b)W + 2(b+y) = 0 # b는 even number
# W = [(2 + b/2) +- sqrt((2+b/2)^2 - 2*2(b+y))] / 2, W >= H


def solution(brown, yellow):
    w = ((2 + brown//2) + int(((2 + brown//2)**2 - 2*2*(brown + yellow))**0.5))//2
    h = ((2 + brown//2) - int(((2 + brown//2)**2 - 2*2*(brown + yellow))**0.5))//2
    # h = (brown + yellow) // w
    answer = [w, h]
    return answer