"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
"""

"""
利用二分查找。如果中间元素值>最后一个元素值，说明最小值右半区间，
            如果中间元素<最后一个元素区间，说明最小值在左半区间，
            如果相等说明有相同元素，需要将判断区间往前缩一下，继续判断，不断循环，
            当二分查找的的左右区间相等了，就说明找到最小值了。
"""


def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    # 二分法 左边 和 右边
    left = 0
    right = len(rotateArray) - 1
    while left < right:
        # 原始数组为非递减数组 向右旋转数组，左侧小的会移到右侧，即旋转后，最左的一定大于等于右侧
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[left]
        # 直接去掉小数除法
        mid = left + (right - left) // 2

        # 左半数组为有序数组 最小值在中间值右方
        if rotateArray[mid] > rotateArray[right]:
            left = mid + 1
        # 右半数组为有序数组 最小值在中间值左边
        elif rotateArray[mid] < rotateArray[right]:
            right = mid
        # 如果中间值 出现和最右值相等，无法确定。 但是相等值肯定在最右或者最左出现连续的同值
        else:
            left = left + 1  # 缩小范围

    return rotateArray[left]


print(minNumberInRotateArray([3, 4, 5, 1, 2]))

# 思路2 遍历，只要找到前后不是呈现递增的那个数就是最小数
