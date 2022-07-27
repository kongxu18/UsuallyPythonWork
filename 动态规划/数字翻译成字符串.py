"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

"""


# 使用动态规划
# 动态转移方程 f(i) = f(i-1)+f(i-2) i-1>=0
class Solution:
    res = []

    def translateNum(self, num: int) -> int:
        if int(num) == 0 or int(num) == 1:
            return 1
        num = str(num)

        return 1


s = Solution()
s.translateNum(12258)
