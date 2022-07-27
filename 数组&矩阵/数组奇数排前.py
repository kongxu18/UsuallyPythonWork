"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。


首尾双指针
i为首指针，j为尾指针，i向前走遇到奇数则跳过，j向后走遇到偶数则跳过。i为偶数且j为奇数时，交换两者的值。继续下一步。
"""


class Solution:
    def exchange(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] % 2 == 1:
                left += 1
            elif nums[right] % 2 == 0:
                right -= 1
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        return nums

    def fun(self, nums):
        # 首尾双指针
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[i] % 2:
                i += 1
                continue
            if not nums[j] % 2:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        return nums
