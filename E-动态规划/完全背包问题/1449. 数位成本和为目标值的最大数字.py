"""
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。



示例 1：

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：
添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。
"977" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5

示例 2：
输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。

示例 3：
输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。

示例 4：
输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"


提示：

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
"""
import sys
from typing import List

"""
思路分析：
1.由于每一个数可以使用多次，符合「完全背包问题」的特征；
2.限制条件是：这些数字消耗的和恰好等于 target；
3.与之前的问题不同的是，本题让我们求出一个具体的解，而不是只问最优解是多少。
  友情提示：动态规划的问题一般只问最优值是多少，而不问具体的解。
4.由于数字的位数决定了数字的大小，位数越多的数字肯定越大。
  因此我们需要 将状态设计成为能够凑成容量的数字的最大位数是多少，然后根据动态规划的结果，再求解题目问的最大整数。
"""


# 方法1：完全背包 + 贪心算法
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # cost = [4,3,2,5,6,7,2,5,5], target = 9
        # 第 1 步：使用动态规划计算最大位数
        # dp[i][j] 表示：使用数组 cost 前缀区间 [0..i] 里的元素能够刚好凑成和为 j 的时候的数字的 最大位数。
        dp = [[-float('inf')] * (target + 1) for _ in range(10)]
        dp[0][0] = 0

        for i in range(1, 10):
            c = cost[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= c and dp[i][j - c] != -float('inf'):
                    dp[i][j] = max(dp[i][j], dp[i][j - c] + 1)
            print(dp)  # [0, -inf, 1, 1, 2, 2, 3, 3, 4, 4]]

        if dp[9][target] < 0:
            return '0'

        # 根据第 1 步计算的结果，优先考虑数值大的放在高位，还原最大整数
        t = target
        res = ''
        # cost = [4,3,2,5,6,7,2,5,5], target = 9
        for i in range(9, 0, -1):
            c = cost[i - 1]
            while t >= c and dp[i][t - c] == dp[i][t] - 1:
                t -= c
                res += str(i)
        return res


# dp空间优化：一维数组
class Solution2:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-float('inf')] * (target + 1)
        dp[0] = 0

        for i in range(1, 10):
            c = cost[i - 1]
            for j in range(c, target + 1):
                dp[j] = max(dp[j], dp[j - c] + 1)

        if dp[target] < 0:
            return "0"

        # 在有结果的前提下，倒序反推路径
        res = ''
        for i in range(9, 0, -1):
            c = cost[i - 1]
            while target >= c and dp[target] == dp[target - c] + 1:
                res += str(i)
                target -= cost[i - 1]

        return res


if __name__ == '__main__':
    cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
    target = 9  # 7772
    # cost = [7, 6, 5, 5, 5, 6, 8, 7, 8]
    # target = 12  # 85
    # cost = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    # target = 5000
    print(Solution().largestNumber(cost, target))
