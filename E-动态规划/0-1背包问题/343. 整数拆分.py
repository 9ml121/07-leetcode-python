"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。

示例 1:
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。


提示:
2 <= n <= 58
"""


# 方法1：dp
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))

        # print(dp)
        return dp[n]


# 方法2：贪心算法
class Solution2:
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3

        res *= n
        return res
