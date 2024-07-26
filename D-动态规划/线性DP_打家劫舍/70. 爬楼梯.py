"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：
1 <= n <= 45
"""

# todo 方法1：动态规划(推荐！)


class Solution:
    def climbStairs(self, n: int) -> int:
        # 每次可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶?

        # dp[i] 表示爬到第 i 阶楼梯的所有方法数
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        # todo 状态转移：只依赖前2个位置dp值,实际上dp可以用2个常数代替
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


    # dp空间优化：滚动变量
    def climbStairs2(self, n: int) -> int:
        # 每次可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶?
        if n == 1:
            return 1

        one = 1   # 第1个台阶（前2个台阶）
        two = 2   # 第2个台阶（前1个台阶）
        for _ in range(3, n + 1):
            tmp = two + one
            one = two
            two = tmp

        return two

# 方法2: 递归
class Solution2:
    from functools import cache

    @cache
    def climbStairs(self, n: int) -> int:
        # 每次可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶?
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)


if __name__ == '__main__':
    sol1 = Solution()
    sol2 = Solution2()
    print(sol1.climbStairs(5))
    print(sol2.climbStairs(5))
