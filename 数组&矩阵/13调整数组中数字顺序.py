"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# res:[1, 3, 5, 7, 9, 2, 4, 6, 8]

def reOrderArray(arr):
    # 奇数
    odd = []
    # 偶数
    even = []
    for i in arr:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd+even


print(reOrderArray(array))
