"""
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1：
输入：a = 2, b = [3]
输出：8

示例 2：
输入：a = 2, b = [1,0]
输出：1024

示例 3：
输入：a = 1, b = [4,3,3,8,5,2]
输出：1

示例 4：
输入：a = 2147483647, b = [2,0,0]
输出：1198


提示：

1 <= a <= 2^31 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b 不含前导 0
"""
from typing import List

"""
1. 如何处理 mod 运算?
由于计算机的编码方式，形如 (a * b) % base 这样的运算，乘法的结果可能导致溢出.

在二分查找中，我们求中点索引时用 (l+r)/2 转化成 l+(r-l)/2，避免溢出的同时得到正确的结果。
模运算的技巧：(a * b) % k = (a % k) * (b % k) % k

换句话说，对乘法的结果求模，等价于先对每个因子都求模，然后对因子相乘的结果再求模。

2. 如何计算指数为很大数字？
3**425 = 3 ** (420 + 5) = (3**42)**10 * (3**5)
"""


class Solution:
    mod = 1337  # 声明一个类变量,表示取模数

    # 计算a的k次方，参考leetcode 50题, 这里是计算a的k次方，然后对1337取模的结果
    def myPow(self, a: int, k: int):
        a %= self.mod
        res = 1
        for i in range(k):
            res *= a
            res %= self.mod
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1

        last = b.pop()  # 取出 b 数组的最后一个元素
        part1 = self.myPow(a, last)  # 计算 a 的 last 次方
        part2 = self.myPow(self.superPow(a, b), 10)  # 递归计算 superPow(a, b[:len(b)-1]) 的 10 次方

        return (part1 * part2) % self.mod  # 返回结果，每次都对结果求模
