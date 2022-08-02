def array_plus(array_input):

    plus_plus = []
    m = 0
    for i in range(len(array_input)-1):
        m += array_input[i]
        if i :
            plus_plus.append( m)
            print(array_input[i])
            print('当前的m值：', m)
            print('当前plus_plus数组中的各个值：',plus_plus)
    print(plus_plus)
    return plus_plus


class A:

    @classmethod
    def fun(cls):
        print(cls)

a = A()
a.fun()
A.fun()
# if __name__ == '__main__':
#     array = [1,2,3,4,5,6]
#     array_plus(array)