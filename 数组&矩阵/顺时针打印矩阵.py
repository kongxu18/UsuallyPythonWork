"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix =  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
  

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length  <= 100
"""

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        count = 0
        times = ((len(matrix[0]) if len(matrix[0]) < len(matrix) else len(matrix)) + 1) // 2
        print(times)
        array = []
        while True:
            left, top, right, bottom = 0 + count, 0 + count, len(matrix[0]) - count, len(matrix) - count
            if count >= times:
                break

            print(matrix[top][left], count, '---')
            l, t, r, b = left, top, right, bottom
            while l < right:
                array.append(matrix[top][l])
                l += 1
            if len(matrix) - count * 2 > 1:
                while t + 1 < bottom:
                    array.append(matrix[t + 1][right - 1])
                    t += 1
                print('right', right, 'left', left)
                if len(matrix[0]) - count * 2 > 1:
                    while r - 1 > left:
                        array.append(matrix[bottom - 1][r - 2])
                        r -= 1
                    while b - 2 > top:
                        array.append(matrix[b - 2][left])
                        b -= 1
            count += 1
        return array


s = Solution()
res = s.spiralOrder(matrix)
print(res)


class Solution2:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i])  # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r: break
        return res


s = Solution2()
res = s.spiralOrder(matrix)
print(res)
