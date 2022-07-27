"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
"""


def numberOf1(n):
    # write code here

    cnt = 0
    if n < 0:
        n = n & 0xffffffff
        # 转为1111 32位，跟1111。。。做与运算，不会改变原来的数值，这里只是转为32位的二进制

    while n:
        print(bin(n))
        """
        整数 3   二进制 0011
            4         0100
        
        
        对于 n ，n-1 做与运算，会把最右边的1消除一个
        """
        n = (n - 1) & n
        cnt += 1

    return cnt


r = numberOf1(-3)
print(r)
# print(r, bin(0xffffffff),len(str(bin(0xffffffff))))
