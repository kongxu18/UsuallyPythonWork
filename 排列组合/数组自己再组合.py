# 先得出数组所有子集
# 通过递归的方式生成子集
import copy
import itertools
import numpy as np


class Solution(object):
    def __init__(self, arg):
        self.arg = arg

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.out = {}
        self.sub(nums, 0, [])
        return self.out

    def sub(self, nums, start, sub):
        if len(sub) != 0:
            r = self.out.get(len(sub))
            if not r:
                self.out[len(sub)] = []

            self.out[len(sub)].append(sub)
        if len(sub) == len(nums):
            return
        for i in range(start, len(nums)):
            self.sub(nums, i + 1, sub + [nums[i]])

    def combinationSum(self, candidates, target):
        # 对candidates进行排序
        candidates.sort()
        path = []
        res = []

        def backwards(start, sum, candidates):
            # sum == target,将path添加到res中
            if sum == target:
                res.append(path[:])
                return
            # 剪枝
            for i in range(start, len(candidates)):
                sum += candidates[i]
                # 剪枝
                # 判断sum是否大于target，因为candidates是从小到大的，
                # 若sum大于target，则不遍历序号i之后的值；
                # 若sum小于target，将candidates[i]添加到path中，然后进行回溯
                if sum <= target:
                    path.append(candidates[i])
                    backwards(i, sum, candidates)
                    path.pop()
                    sum -= candidates[i]
                else:
                    return

        backwards(0, 0, candidates)
        return res

    def deal(self):
        child_list: dict = self.subsets(self.arg)

        add_list = self.combinationSum(list(child_list.keys()), len(self.arg))

        print(child_list)
        print(add_list)
        print([len(n) for n in add_list])

        # 结果集合
        result = []
        result.append(child_list[1])
        result.append(child_list[len(self.arg)])
        for model in add_list:

            if len(model) == len(self.arg) or len(model) == 1:
                continue
            else:
                model_dic = {}
                for m in model:
                    if model_dic.get(m):
                        model_dic[m] += 1
                    else:
                        model_dic[m] = 1
                self.calculate_groups(model_dic, self.arg, child_list)
            break

    @staticmethod
    def combinations(li, num):
        res = np.array([])
        for i in itertools.combinations(li, num):
            arr = np.array(i)
            arr = arr.reshape(-1)

    def calculate_groups(self, model_dic, arr, child_list):
        # 根据模式计算组合
        groups = []
        print(model_dic, '模式')

        # 原本的数组
        init_choice = arr[:]

        for number in range(4, 0, -1):
            # 从 大 到 小 从4 到 1，可以降低笛卡尔乘机
            times = model_dic.get(number)
            if times:
                li = child_list[number]
                for i in itertools.combinations(init_choice, number):
                    groups.append(i)
            break

        def back(groups, model_li):
            ...

        print(groups)
        print(len(groups))


arg = ['a', 'b', 'c', 'd', 'e']

s = Solution(arg)
r = s.deal()

print(r)
