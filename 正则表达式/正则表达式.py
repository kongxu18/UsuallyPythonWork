"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。

例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

从后往前判断
"""
A = 'aaaabbc'
B = "a*bb."
import numpy as np


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1

        # 初始化一个矩阵
        match = np.zeros((m, n), dtype=np.bool)
        match[0][0] = True
        for i in range(m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    #     * 号绝不会出现在第一个，这样匹配表达式就是错的
                    match[i][j] |= match[i][j - 2]
                    if i > 0:
                        kk, aa = p[j - 1], s[i - 1]
                        if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                            match[i][j] |= match[i - 1][j]
                else:
                    # 不为* 并且是第一行，直接跟空字符串匹配，那就是false
                    # 默认都是false 直接pass掉
                    if i != 0:
                        if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                            match[i][j] = match[i - 1][j - 1]
        print(match)
        return match[m - 1][n - 1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


sol = Solution()
res = sol.isMatch(A, B)

sol2 = Solution2()
res2 = sol2.isMatch(A, B)

print(res, res2)
