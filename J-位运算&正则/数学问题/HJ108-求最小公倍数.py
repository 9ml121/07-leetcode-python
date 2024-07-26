"""
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围：1≤a,b≤100000
输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。
"""


# 解法1: a <= b, 最大公倍数为a*b, 最小公倍数为b
def getResult1(a: int, b: int):
    # 保证较大数为b
    if a > b:
        a, b = b, a

    for num in range(b, a * b + 1, b):
        if num % a == 0:
            return num


# todo 解法2：要求两个正整数的最小公倍数(LCD)，可以使用最大公约数（GCD）来计算。
# 根据数学原理，两个数的最小公倍数等于它们的乘积除以最大公约数。

# gcd 函数用于计算两个数的最大公约数，采用的是欧几里得算法
# 这里可以直接调用库包：math.gcd(6,9)
def gcd(a:int, b:int)->int:  # a = 6, b = 9
    while b != 0:
        a, b = b, a % b  # a=9,b=6 ==> a=6,b=3 ==> a=3,b=0
    return a


# lcm 函数接受两个参数 a 和 b，分别表示两个正整数，它通过先计算乘积 a * b，
# 然后除以它们的最大公约数 gcd(a, b) 得到最小公倍数。
def lcm(a:int, b:int)->int:
    return (a * b) // gcd(a, b)  # (6*9)//3


if __name__ == '__main__':
    # a, b = map(int, input().split())
    print(getResult1(6, 9))
    print(getResult1(7, 5))
    print("-----------")
    print(gcd(6, 9))
    print(gcd(9, 6))
    print(gcd(5, 7))
    print(lcm(3, 9))
    print(lcm(7, 5))
