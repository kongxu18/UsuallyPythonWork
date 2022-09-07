import itertools
from typing import List


def combinationSum(candidates, target):
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
            cur = candidates[i]
            if cur > 4:
                continue
            sum += cur

            # 剪枝
            # 判断sum是否大于target，因为candidates是从小到大的，
            # 若sum大于target，则不遍历序号i之后的值；
            # 若sum小于target，将candidates[i]添加到path中，然后进行回溯
            if sum <= target:
                path.append(cur)
                backwards(i, sum, candidates)
                path.pop()
                sum -= cur
            else:
                return

    backwards(0, 0, candidates)
    return res


a = ['a', 'b', 'c', 'd']

l = itertools.permutations(a)
print(list(l))

add_list = combinationSum([i for i in range(1, len(a) + 1)], len(a))
print(add_list)

#
# add_list = combinationSum([i for i in range(1, 25)], 24)
# print(add_list)
#
# add_list = combinationSum([i for i in range(1, 9)], 9)
# print(add_list)
#
# add_list = combinationSum([i for i in range(1, 10)], 10)
# print(add_list)


def deal(add_list, arr):
    add_list.sort(reverse=True)
    need = arr[:]

    for num in add_list:
        ...



deal(add_list[1], a)
