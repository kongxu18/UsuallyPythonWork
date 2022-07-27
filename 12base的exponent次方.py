"""
给定一个double类型的浮点数base
      和int类型的整数exponent。
求base的exponent次方。
"""


def power(base, exponent):
    return base ** exponent


def power2(base, exponent):
    if exponent == 1:
        return base

    result = base

    if exponent > 0:
        for i in range(2, exponent + 1):
            result *= base

    elif exponent < 0:
        for i in range(2, abs(exponent) + 1):
            result *= base
            result = 1.0 / result
    else:
        result = 1

    return result


print(power(5, -2), power2(5, -2))
