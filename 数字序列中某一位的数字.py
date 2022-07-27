"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。


示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 位数，起始值，计算多少位
        digit, start, count = 1, 1, 9

        while n > count:
            n -= count
            start *= 10  # 1, 10, 100, ...
            digit += 1  # 1,  2,  3, ...
            count = 9 * start * digit  # 9, 180, 2700, ...

        # 从0开始
        n = n - 1
        n_int = n // digit
        n_remainder = n % digit
        number = str(range(start, start * 10)[n_int])[n_remainder]
        return int(number)


s = Solution()
s.findNthDigit(15)
