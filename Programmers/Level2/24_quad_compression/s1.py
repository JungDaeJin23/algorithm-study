# quad tree?
# fractal structure => recursion
# first quad row major search, if match wrong split


def quad(arr):
    standard_element = arr[0][0]
    flag = True

    i = 0
    while i < len(arr) and flag:
        j = 0
        while j < len(arr[i]) and flag:
            if arr[i][j] != standard_element:
                flag = False
            j += 1
        i += 1

    if flag:
        a = [standard_element]
    else:
        # split
        n = len(arr) // 2
        quad1 = []
        quad2 = []
        quad3 = []
        quad4 = []
        i = 0
        while i < len(arr):
            j = 0
            forward = [0 for _ in range(n)]
            backward = [0 for _ in range(n)]
            while j < len(arr[i]):
                # # the second quadrant
                # if i < n and j < n:
                #     quad2
                # # the first quadrant
                # elif i >= n and j < n:
                #     pass
                # # the forth quadrant
                # elif i >= n and j >= n:
                #     pass
                # # the third quadrant
                # else:
                #     pass

                # making list to put list type // make a multi dimensional array
                if j < n:
                    forward[j] = arr[i][j]
                else:
                    backward[j - n] = arr[i][j]
                j += 1
            if i < n:
                quad1.append(backward)
                quad2.append(forward)
            else:
                quad3.append(forward)
                quad4.append(backward)
            i += 1
        a = []
        a.extend(quad(quad1))
        a.extend(quad(quad2))
        a.extend(quad(quad3))
        a.extend(quad(quad4))
    return a


def solution(arr):

    a = quad(arr)
    answer = [0, 0]
    for element in a:
        answer[element] += 1

    return answer


if __name__ == "__main__":
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
