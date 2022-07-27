"""
经典排序
"""


def bubbleSort(array):
    """
    冒泡排序
    :param array: 数组
    :return: 排序后数组
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# -------------------------------------------------
def selectionSort(array):
    """
    选择排序
    :param array: 数组
    :return: 排序后数组
    """
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array


# ------------------------------------------------
def insertionSort(array):
    """
    插入排序 从被排过的部分序列后往前扫描，把后面的值插入前面已排序的当中
    :param array:
    :return:
    """
    for i in range(1, len(array)):
        # 选择最后的一个插入前面 一开始从第二个元素开始
        key = array[i]  # 1 key 3
        # j 为插入位置
        j = i - 1  # 0
        while j >= 0:
            selectNum = array[j]
            if selectNum > key:
                array[j + 1] = selectNum
            else:
                break
            j -= 1
        array[j + 1] = key
    return array


# -----------------  快排
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")


if __name__ == '__main__':
    import copy

    arr = [9, 3, 6, 7, 2, 5, 4, 8, 0, 1]
    print(arr, 'ttt')
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)

    print(bubbleSort(arr))
    print(selectionSort(arr2))
    print(insertionSort(arr3))
