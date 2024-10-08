"""
描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的 n （ n 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。


数据范围： 1≤n≤100  ，输入的数据大小满足 2≤value≤30000
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。

输入：
4
2 5 6 13
输出：
2

输入：
2
3 6
输出：
0
"""

'''
解法
重点是
    如何判断是素数？
    如何判断偶数？
    如何判断奇数？
    采用二分图、匈牙利算法查找最优组合。

标准的二分图写法
先将奇偶数分组，然后寻找匹配的边，即寻找和为素数的匹配，然后存入二分图中，标准的匈牙利搞定
'''


# 判断一个数是否是质数
def is_prime(num: int):
    primes = [True] * (num + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, num + 1, i):
                primes[j] = False
    return primes[num]


# print(is_prime(4))

# n = int(input())
# nums = list(map(int, input().split()))
n = 4
nums = [2, 5, 6, 13]
# 2 5 6 13
# 从一个数组中取出任意2个元素，一共      有哪些组合？（数组元素是否有重复）==》递归+回溯
# 正偶数 n ，表示待挑选的自然数的个数 1≤n≤10
# 输入的数据大小满足 2≤value≤30000
# 全局变量
res = []
# 局部变量
path = []


def helper(nums, path: list, res: list):
    # 叶子节点
    if len(path) == 2:
        res.append(path)
        return
    for i in range(len(nums)):
        helper(nums[i + 1:], path + [nums[i]], res)


helper(nums, path, res)
print(res)
