def permutation(s):
    c, res = list(s), []

    def recur(x):
        if x == len(c) - 1:
            res.append(''.join(c))  # 添加排列方案
            return
        dic = set()
        for i in range(x, len(c)):
            if c[i] in dic:
                continue
            dic.add(c[i])
            c[i], c[x] = c[x], c[i]
            recur(x + 1)
            c[i], c[x] = c[x], c[i]

    recur(0)
    return res


import copy


def calculate_add_combination(n):
    res_list = []
    tmp_list = []

    def num_to_n(n, tmp_list, start):
        if n == 1:
            tmp = copy.deepcopy(tmp_list)
            tmp.append(1)
            res_list.append(tmp)
        else:
            for i in range(start, n):
                tmp_list.append(i)
                num_to_n(n - i, tmp_list, i)
                tmp_list.remove(tmp_list[-1])

            tmp = copy.deepcopy(tmp_list)
            tmp.append(n)
            res_list.append(tmp)

    num_to_n(n, tmp_list, 1)
    # duplicate remove
    res_list = duplicate_remove(res_list, n)
    return res_list


def duplicate_remove(a_list, n):
    len_list = len(a_list)
    for i in range(len_list - 1, -1, -1):
        # remove list which equal to its own
        if len(a_list[i]) == 1:
            a_list.remove(a_list[i])
            continue
        for j in range(i):
            if set(a_list[i]) == set(a_list[j]):
                a_list.remove(a_list[i])
                break
    return a_list


def clear_list(data):
    new_data = []
    for i in range(len(data)):
        src = data[i]

        is_repeat = False
        for j in range(len(new_data)):
            temp = new_data[j]

            # 二维数组内元素数组再比对
            wid = 0
            for t in temp:
                if t in src:
                    wid += 1
            if wid == len(src):
                is_repeat = True

        if not is_repeat:
            new_data.append(src)

    return new_data


def group(sorts, add_groups, original_data: list):
    res = []
    for group in add_groups:
        # 选择排列模式
        if len(group) == len(original_data):
            # 表示 1，1，1... 有且只有一种
            temp = [set(i) for i in sorts[0]]

            res.append(temp)
            # print(sorts[0],set(sorts[0]))
            res.append([set(sorts[0])])
            continue
        # 其余位数的排列需要考虑组合的不同

        for sort in sorts:
            # 对全排列结果 划分组合
            sort = list(sort)
            start_i = 0
            end_i = 0
            s = []
            for num in group:
                end_i += num
                s.append(set(sort[start_i:end_i]))

                start_i = end_i

            res.append(s)
    res = clear_list(res)
    return res


if __name__ == '__main__':
    # 所有排序
    arg = ['a', 'b', 'c', 'd']
    all_sorts = permutation(arg)
    print(all_sorts)

    l = len(arg)

    add_group = calculate_add_combination(l)
    print(add_group)

    final = group(all_sorts, add_group, arg)

    print(final)
    print(len(final))



