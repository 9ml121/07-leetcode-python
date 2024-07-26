""" 
题目描述
RSA加密算法在网络安全世界中无处不在，它利用了极大整数因数分解的困难度，数据越大，安全系数越高，给定一个 32 位正整数，请对其进行因数分解，找出是哪两个素数的乘积。

输入描述
一个正整数 num 0 < num < 2147483647

输出描述
如果成功找到，以单个空格分割，从小到大输出两个素数，分解失败，请输出-1, -1

用例
输入	15
输出	3 5
输入	27
输出	-1 -1
"""
import math
num = int(input())


def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


a, b = -1, -1
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0 and isPrime(i) and isPrime(num//i):
        a, b = [i, num//i]
        break
print(f'{a} {b}')
