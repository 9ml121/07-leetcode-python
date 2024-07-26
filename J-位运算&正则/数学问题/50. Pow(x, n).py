"""
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


提示：
-100.0 < x < 100.0
-231 <= n <= 231-1
n 是一个整数
要么 x 不为零，要么 n > 0 。
-10^4 <= x^n <= 10^4
"""


# 方法1: 调用内置函数
# return x ** n
# return math.pow(x,n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        elif n < 0:
            return self.myPow(1 / x, -n)

        else:
            if n % 2 == 0:
                sub = self.myPow(x, n // 2)
                return sub * sub
            else:
                return x * self.myPow(x, n - 1)