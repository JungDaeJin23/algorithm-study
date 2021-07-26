def power(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def power_version2(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0

    if exponent % 2 == 0:
        new_base = power_version2(base, exponent//2)
        return new_base * new_base
    else:
        new_base = power_version2(base, (exponent-1)//2)
        return new_base * new_base * base

print(power_version2(2, 10))