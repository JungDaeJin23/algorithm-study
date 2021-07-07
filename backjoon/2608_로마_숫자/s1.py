# 두 수를 더한 값을 첫째 줄에 아라비아숫자로 출력하고 둘째 줄에는 로마 숫자로 출력한다.
transfer_rule_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_2_int(str1):
    global transfer_rule_dict
    before_num = 1000
    total = 0
    for alpha in str1:
        num = transfer_rule_dict[alpha]
        if num > before_num:
            total -= before_num
            total += num - before_num
        else:
            total += num
        before_num = num
    return total


# IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
def int_2_roman(num):
    roman_num = ''
    digit = 1000
    while digit:
        quotient = num // digit
        if quotient:
            if digit == 1000:
                roman_num += 'M' * quotient
            elif digit == 100:
                if quotient == 9:
                    roman_num += 'CM'
                elif quotient == 4:
                    roman_num += 'CD'
                else:
                    if quotient < 4:
                        roman_num += 'C'*quotient
                    else:
                        roman_num += 'D' + 'C'*(quotient-5)
            elif digit == 10:
                if quotient == 9:
                    roman_num += 'XC'
                elif quotient == 4:
                    roman_num += 'XL'
                else:
                    if quotient < 4:
                        roman_num += 'X'*quotient
                    else:
                        roman_num += 'L' + 'X'*(quotient-5)
            else:
                if quotient == 9:
                    roman_num += 'IX'
                elif quotient == 4:
                    roman_num += 'IV'
                else:
                    if quotient < 4:
                        roman_num += 'I'*quotient
                    else:
                        roman_num += 'V' + 'I'*(quotient-5)
        num %= digit
        digit //= 10
    return roman_num


roman_num1 = input()
roman_num2 = input()
sum_num = roman_2_int(roman_num1) + roman_2_int(roman_num2)
print(sum_num)
print(int_2_roman(sum_num))