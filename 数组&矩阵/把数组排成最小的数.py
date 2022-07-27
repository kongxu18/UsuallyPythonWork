"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

输入: [10,2]
输出: "102"
示例2:

输入: [3,30,34,5,9]
输出: "3033459"

"""


class Solution:
    """
    自定义快排方法
    """

    def minNumber(self, arr) -> str:

        def quick_sort(arr, i, j):
            if i >= j:
                return
            pivot = arr[i]
            low = i
            high = j
            while i < j:
                while int(arr[j] + pivot) >= int(pivot + arr[j]) and i < j:
                    j -= 1
                arr[i] = arr[j]
                while int(arr[i] + pivot) <= int(pivot + arr[i]) and i < j:
                    i += 1
                arr[j] = arr[i]
            arr[j] = pivot

            quick_sort(arr, low, i - 1)
            quick_sort(arr, i + 1, high)
            return arr

        arr = [str(i) for i in arr]
        quick_sort(arr, 0, len(arr) - 1)
        return ''.join(arr)


s = Solution()
r = s.minNumber([1,1,1])
print(r)