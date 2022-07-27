"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""
from 排序 import bubbleSort

LIST = [2, 3, 1, 0, 2, 5, 3, 4, 6, 7, 5]

print(LIST)


# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    duplication = []

    def duplicate(self, numbers):
        """
        排序数组 ，比较前后两个就可以
        :param numbers:
        :return:
        """
        if numbers is None or len(numbers) <= 1:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
        # 排序
        # numbers.sort()
        numbers = bubbleSort(numbers)
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                self.duplication.append(numbers[i])
        return False

    def duplicate_hash(self, numbers):
        """
        使用哈希结构
        借用一个集合，每次将数字和集合比较，有的就是重复的，没有的加入集合
        :param numbers:
        :param duplication:
        :return:
        """
        if numbers is None or len(numbers) <= 1:
            return False

        usedDic = set()  # 集合
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
            if numbers[i] not in usedDic:
                usedDic.add(numbers[i])
            else:
                self.duplication.append(numbers[i])
        return False


S = Solution()
S.duplicate_hash(LIST)
print(S.duplication)
