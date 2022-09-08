# 先得出数组所有子集
# 通过递归的方式生成子集
import copy
import itertools
import numpy as np
from typing import List
import pandas as pd


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
        # child_list: dict = self.subsets(self.arg)

        add_list: List[List] = self.combinationSum([num for num in range(1, len(self.arg) + 1)], len(self.arg))

        print(add_list, '组成模式')

        # 结果集合
        result = []

        for model in add_list:

            if len(model) == len(self.arg) or len(model) == 1:
                continue
            else:
                # 把model 进行反转
                model.sort(reverse=True)

                two_dimensional_arr = self.calculate_groups(model, self.arg)
                self.clear_dataframe(model, two_dimensional_arr)

    def clear_dataframe(self, model, arr):
        # 把二维数组根据模式转 成dataframe 并 去重

        df = pd.DataFrame(data=arr)
        array = np.array(arr, dtype='str')

        # clear_arr = np.char.add(array[:,[0,1]])

        cursor = 0
        name_dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        for num in model:
            df[name_dic[num]] = df[cursor]

            cursor += 1
            for i in range(1,num):
                df[name_dic[num]] += df[cursor]
                cursor += 1
            name_dic[num] += '1'

        print(df.iloc[:,cursor:])

        # print(clear_arr,'=-=-=-=-=-=-=')
        print(array)


    def calculate_groups(self, model, arr):
        # 根据模式计算组合
        groups = []
        print(model, '模式')

        # 原本的数组
        init_arr = set(arr[:])
        if not groups:
            for item in itertools.combinations(init_arr, model[0]):
                groups.append([*item])

        res = []

        def back(groups, model, m_index):

            temp = []
            if m_index > len(model) - 1:
                res[:] = groups
                return

            cur = model[m_index]

            for i, now_arr in enumerate(groups):
                turn_now_set = set(now_arr)

                useful_arr = init_arr - turn_now_set

                for tup in itertools.combinations(useful_arr, cur):
                    union_arr = now_arr + list(tup)

                    temp.append(union_arr)

            m_index += 1

            back(temp, model, m_index)

        back(groups, model, 1)

        print(res)
        return res


arg = ['a', 'b', 'c', 'd']

s = Solution(arg)
r = s.deal()
