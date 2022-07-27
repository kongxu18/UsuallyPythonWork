"""
用小矩形覆盖大矩形

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
依然是斐波那契数列

同理青蛙跳阶
"""


def rectCover(number):
    """
    动态规划
    :param self:
    :param number:
    :return:
    """
    if number <= 0:
        return 0
    elif number <= 2:
        return number

    first = 1
    second = 2
    result = 0
    for i in range(3, number + 1):
        result = first + second
        first, second = second, first + second

    return result


# 8 34
print(rectCover(5), rectCover(8))
