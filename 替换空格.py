"""
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
STRING = 'We Are Happy'


def replaceSpace(s, method=1):
    if method:
        # 另外一种方法
        return s.replace(' ', '%20')
    arr = s.split(' ')
    print(arr)
    s = '%20'.join(arr)
    return s


print(replaceSpace(STRING))


def replaceSpace_method2(s):
    """
    新建一个数据，从后往前遍历，跟原始字符串比较。遇到空格就换成替换字符，其余直接copy进去。
    新建长度 = 原始的 + 空格数*2
    :param s:
    :return:
    """
    array = []
    for i in range(-1, -len(s)-1, -1):
        if s[i] == ' ':
            array.insert(0, '%20')
        else:
            array.insert(0, s[i])
    print(array)
    return ''.join(array)


r = replaceSpace_method2(STRING)
print(r)