def solution(s):
    num_alpha = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                 'eight': '8', 'nine': '9'}

    answer = ''
    tmp = ''
    ''.isalpha()
    for el in s:
        if el.isdigit():
            answer += el
        else:
            tmp += el
            alpha = num_alpha.get(tmp)
            if alpha:
                answer += alpha
                tmp = ''
    return int(answer)
