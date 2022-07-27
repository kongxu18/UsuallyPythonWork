"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
import numpy as np

K = 8
m, n = 11, 16
mat = np.zeros(m * n)
mat.shape = m, n


class Solution:
    def __init__(self, mat, k):
        self.mat = mat
        self.row_len, self.col_len = self.mat.shape
        self.k = k
        self.passed = []

    def moving(self, row, col, k):
        count = self.sum_number(row) + self.sum_number(col)
        if count <= k:
            self.mat[row][col] = 1
            self.passed.append((row, col))
            for i in (-1, 1):
                if 0 <= col + i < self.col_len and (row, col + i) not in self.passed:
                    # 左右
                    self.moving(row, col + i, k)

                if 0 <= row + i < self.row_len and (row + i, col) not in self.passed:
                    # 上下
                    self.moving(row + i, col, k)
        return

    def sum_number(self, num):
        n = 1
        count = 0
        while num > 0:
            count += num % 10
            num = num // 10
            n += 1
        return count


def sum_num2(num, count):
    if num == 0:
        return count
    count += num % 10
    num = num // 10
    return sum_num2(num, count)


s = Solution(mat, K)
s.moving(0, 0, K)
print(s.mat)

t = np.zeros(m * n)
t.shape = m, n
for row in range(m):
    for col in range(n):
        t[row][col] = sum_num2(row, 0) + sum_num2(col, 0)
print(t)

res = np.sum(s.mat)
print('一共可以走到的格数：', res)
