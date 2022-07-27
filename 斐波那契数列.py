"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39 n=0时，f(n)=0 n=1时，f(n)=1 n>1时，f(n)=f(n-1)+f(n-2)
"""


# 递归实现
def fib(n):
    """
    :param n: 索引值
    :return: 索引对应的数值
    """
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    # return fib(1)+fib(0)+fib(1)+fib(1)+fib(0)+fib(1)+fib(0)+1


l = fib(5)
print(l)


def fib2(n):
    a, b = 0, 1
    for i in range(n):
        # 自身进行重复累加
        print(b, end=' ')
        a, b = b, a + b


fib2(1)


# 0 1 1 2 3
def fib3(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    print('for')
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b, ' ', end='')


fib3(4)


def fib_4(n):
    """
    yield
    :param n:
    :return:
    """
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


print('yield')
for i in fib_4(20):
    print(i, end=' ')
