"""
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
- 假设每一种面额的硬币有无限个。!!
- 题目数据保证结果符合 32 位带符号整数。


示例 1：
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2：
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

示例 3：
输入：amount = 10, coins = [10]
输出：1


提示：
1 <= coins.n <= 300
1 <= coins[i] <= 5000
coins 中的所有值 互不相同
0 <= amount <= 5000
"""
from typing import List

"""
转换成为「完全背包」问题：
1.使用若干个不同面值的硬币凑出总面值为刚好为 amount ，等价于使用若干个物品填满 恰好 重量为 amount 的背包，这里 amount 是约束；
2.目的是找所有的总数，对应「完全背包问题」中找最优解；
3.硬币的选取是 组合（不计较顺序），对应于「完全背包问题」中，物品的组合也不计较顺序。

"""


# 完全背包（二维数组：状态数组多设置一行的写法）
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 计算可以凑成总金额的硬币组合数
        n = len(coins)
        # 定义：使用区间 [0..i) 里的硬币，恰好可以凑出面值为 j 的方案总数
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # base case
        # coin = 0，j > 0, 返回0
        # coin >=0, j = 0, 能凑成的组合数为1(硬币都不装进背包)
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # 不选，复制上一行
                dp[i][j] = dp[i - 1][j]
                # 加入这枚硬币，能凑成w的组合数
                # 由于可以复选，所以是继续在本行查找剩余金币组合数
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        # 返回结果:总得组合数
        return dp[n][amount]


# 降低空间复杂度
# dp 数组的转移只和 dp[i][..] 和 dp[i-1][..] 有关，所以可以进一步降低算法的空间复杂度：
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        # 计算可以凑成总金额的硬币组合数
        n = len(coins)
        dp = [0] * (amount + 1)
        # dp[j]:能凑成金额为j的组合数

        # base case
        dp[0] = 1

        for i in range(n):
            # 从 coins[i] 开始即可
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

            # print(dp)  coins = [1, 2, 5]  amount = 5
            # [1, 1, 1, 1, 1, 1]
            # [1, 1, 2, 2, 3, 3]
            # [1, 1, 2, 2, 3, 4]

        return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]  # 4
    print(Solution().change(amount, coins))
    print(Solution2().change(amount, coins))
