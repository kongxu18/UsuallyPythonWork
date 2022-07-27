"""
给你一根长度为n的绳子，请把绳子剪成m段(m,n都是整数，且n>1,m>1),
每段绳子的长度记为k[0],k[1],k[2],...,k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2，3，3的三段，此时得到的最大乘积为18。
"""

"""
动态规划

定义数组dp，dp[n]表示绳子长度为n时，分割后每一段乘积的最大值；
n == 2和n == 3时，只能切一刀，最大乘积分别为1和2；
n == 4时，若切一刀，有两种情况：1和3及2和2，这个时候就没有必要对3再切了，也没有必要对2切了，最大乘积就是4；
n == 5时，若切一刀，有1和4，2和3，3和2，4和1，只相当于两种情况，也没有必要再切了。
所以当n >= 4的时候，如果切下来有长度为2或3的段时，就没有必要再切了，用数组表示就是

dp[1] = 1，dp[2] = 2，dp[3] = 3，这里一定要上述步骤2区分开，这里是n >= 4时的情况，
在这种情况下，对绳子切割，出现了长度为2或3的段，这时候就不用再对长度为2或3的段切割了，直接返回它们的长度即可。

i从4开始的原因是4以及4之后的长度都有多种可能，需要使用前面的值计算。3也有两种可能，但是3不能使用循环计算的原因是，使用这个循环得到的结果是正确值，
但是3后面的全部都会错，这个products数组书上已经说了是把长度为i的绳子剪成若干段（若干>=1）之后各段长度乘积的最大值。
products[3]=3原因就是后面计算的时候用到f(3)，那说明这个就可以等于3，已经切过了，但是如果是函数一开始长度就是3，根据题目要求，一刀不切是不行的。

简单说，就是直接算f(3)不等于3，但是f(4)里的f(3)可以等于3
————————————————


"""
# 绳子长度
N = 8


def maxProductAfterCut(n):
    # 动态规划
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    products = [0] * (n + 1)
    # 如果剪下一刀，剩下一段为1米的绳子则不需再剪；
    # 如果剪下一刀，剩下一段为2米的绳子则不需再剪；
    # 如果剪下一刀，剩下一段为3米的绳子则不需再剪；
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, n + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > max:
                max = product
        products[i] = max
    print(products)
    return products


maxProductAfterCut(N)


def max_product_after_cutting(n):
    # 如果剪下一刀，剩下一段为1米的绳子则不需再剪；
    # 如果剪下一刀，剩下一段为2米的绳子则不需再剪；
    # 如果剪下一刀，剩下一段为3米的绳子则不需再剪；
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = [0, 1, 2, 3]
    for ni in range(4, n + 1):
        max_value = 0
        for nj in range(1, ni // 2 + 1):
            current = res[nj] * res[ni - nj]

            if current > max_value:
                max_value = current
            else:
                break
        res.append(max_value)
    print(res)
    return res[-1]


print(max_product_after_cutting(8))
