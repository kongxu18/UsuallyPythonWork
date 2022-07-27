"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如
a b c e
s f c s
a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
"""
思路：
    回溯法：首先任意一个点都有可能成为起点，所以要获得任意一点的坐标(位于第几行，第几列)
 * 其次要有一个数组记录这个点是否被访问过，同时要有一个指针来记录字符串中字符的位置。
 * 当某个点成为合法的起点时，即这个点与字符串中第一个字符相等，则可以继续朝上下左右搜索下一个点；
 * 如果这个点不能成为合法的起点，则恢复现场(这个点没有被访问过且字符串指针后退)
"""
import numpy as np

# 创建一个矩阵
str_ = 'bf23'
mat1 = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', '1', '2', '3', '4']
matrix = np.array(mat1, dtype=np.str)
matrix.shape = 3, 4
print(matrix)


# 行，列

class Solution:

    def __init__(self, char, mat):
        self.char = char
        self.mat = mat
        self.row_len, self.col_len = self.mat.shape
        self.start_point = []
        self.passed_path = []

    def get_fpoint(self):
        f_char = self.char[0]
        self.start_point = np.argwhere(self.mat == f_char)
        if not self.start_point.size:
            return False

        count = 0
        while count < len(self.start_point):
            self.passed_path = []
            length = self.handle(self.start_point[count], 1)
            print('length,', length, )
            count += 1
            if length == len(self.char):
                print('成功了')
                return
        print('失败了没有')
        return False

    def handle(self, point, length):
        row, col = point[0], point[1]
        self.passed_path.append((row, col))

        print('point', row, col, self.mat[row][col])
        if length < len(self.char):
            char = self.char[length]
            for i in [-1, 1]:
                if 0 <= col + i < self.col_len:
                    if char == self.mat[row][col + i] and (row, col + i) not in self.passed_path:
                        print(self.passed_path, row, col + i)
                        return self.handle((row, col + i), length + 1)
                if 0 <= row + i < self.row_len:
                    if char == self.mat[row + i][col] and (row + i, col) not in self.passed_path:
                        print(self.passed_path, row + i, col)
                        return self.handle((row + i, col), length + 1)
            else:
                return length
        else:
            return length


s = Solution(str_, matrix)
s.get_fpoint()
print(s.passed_path)
