"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
ARRAY = [[1, 2, 3, 4, 5],
         [10, 11, 12, 13, 14],
         [30, 31, 32, 33, 34]]


def find(target, array):
    # write code here
    m, n = len(array), len(array[0])
    for i in range(m):
        for j in range(n):
            if array[i][j] == target:
                return True
    return False


"""
更好的思路，选取最右上的点，如果小于右上的点，往左走，大于右上点，往下走。
若找不到，然后 / 顺着对角线依次遍历
"""


# array 二维列表
def find_from_rt(target, array):
    # 获取行列
    row, column = len(array), len(array[0])
    print(row, column)
    r = 0
    c = column - 1
    while r < row and c > 0:
        rt_N = array[r][c]
        # print(rt_N)
        # 判断
        if target < rt_N:
            # 往左
            for i in range(c):
                num = array[r][i]
                if num == target:
                    return r, i

        elif target > rt_N:
            # 往下
            for i in range(r):
                num = array[i][c]
                if num == target:
                    return i, c
        elif target == rt_N:
            return r, c
        c -= 1
        r += 1
    return False


res = find_from_rt(30, array=ARRAY)
print(res)
