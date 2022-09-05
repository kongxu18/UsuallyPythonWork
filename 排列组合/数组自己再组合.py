# 先得出数组所有子集
# 通过递归的方式生成子集
import copy


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

        # 结果集合
        result = []
        result.append(child_list[1])
        result.append(child_list[len(self.arg)])
        for group in add_list:
            print(group)
            if len(group) == len(self.arg) or len(group) == 1:
                pass
            else:
                ...
        print(result)
        #     ...


arg = ['a', 'b', 'c', 'd']

s = Solution(arg)
r = s.deal()

print(r)
