"""
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

示例 1：
输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。

示例 2：
输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。


提示：
1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
"""
from typing import List

# 参考474题解题思路
"""
最后要不要对0-n求和，取决于dp数组的定义和边界条件。
1.仅初始化  dp[0][0][0] = 1，dp数组表示的意思是，进行前 i 种工作，恰好使用 j 个人，工作利润至少为 k 的情况数量。 
2.初始化整个dp[0][j][0] = 1，dp数组表示的意思是，进行前 i 中工作，使用 j 个人，工作利润至少为 k 的情况数量。

若定义dp[i][k]为“最多使用 i 个人，利润大于等于 k 的方案数”时，边界条件为：对于每个 i ，dp[i][0]=1。
    对于这种定义，结果返回dp[n][minProfit]即可。 
若定义dp[i][k]为“刚好使用 i 个人，利润大于等于 k 的方案数”时，边界条件为：i=0时, dp[0][0] = 1， i>0时, dp[i][0] = 0。
    解释是：因为初始状态没有任务，刚好使用的人的个数只能为0。执行0个任务却使用了 i (i>0) 个人的情况不可能出现，因此i>0的dp[i][0] = 0。
    对于这种定义，结果需要统计刚好使用了0-n个人，满足条件的方案数的总和。
"""


# dp:三维数组，最后结果需要累加求和
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 1.参与人数限制 <= n
        # 2.总利润 >= minProfit
        # 3.可以选择的工作数量 = jobs
        jobs = len(group)
        MOD = 10 ** 9 + 7
        # dp[i][j][k] 表示在前 i 个工作中 恰好 选择了 j 个员工，并且满足工作利润至少为 k 的情况下的盈利计划的总数目
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(jobs + 1)]
        dp[0][0][0] = 1

        # 阶段：当前选择的工作数量
        for i in range(1, jobs + 1):
            # 维度1:已选择的小组员工人数
            for j in range(n + 1):
                # 维度2:目前状态的工作获利下限
                for k in range(minProfit + 1):
                    # 不选择第 i 个工作
                    dp[i][j][k] = dp[i - 1][j][k]
                    # 选择第 i 个工作
                    if j >= group[i - 1]:
                        # 我们需要满足两个条件才能选择第 k 个工作：
                        # 1.参与人数 j 大于等于第 i 个工作所需的人数 group[i-1]，
                        # 2.利润至少为 k - profit[i-1]
                        # todo 注意:如果 k - profit[i-1] 小于零，表示无法达到利润要求，所以我们需要取 max(0, k - profit[i-1])。
                        dp[i][j][k] += dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]
                    dp[i][j][k] % MOD
        # 计算满足要求的方案数
        res = sum(dp[jobs][j][minProfit] for j in range(n + 1))
        return res % MOD


# 空间优化：逆序遍历,最后结果不需要累加求和
class Solution2:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        # 1.参与人数限制 <= n
        # 2.总利润 >= minProfit
        # 3.可以选择的工作数量 jobs = len(profit)
        """
        jobs = len(group)
        MOD = 10 ** 9 + 7
        # dp[j][k] 表示 最多 选择了 j 个员工，并且满足工作利润至少为 j 的情况下的盈利计划的总数目
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        # 对于最小工作利润 k 为 0 的情况，无论当前在工作的员工有多少人，我们总能提供一种方案，所以初始化 dp[j][0]=1
        for j in range(n + 1):
            dp[j][0] = 1

        # 阶段：当前选择的工作数量
        for i in range(jobs):
            # 维度1:已选择的小组员工人数, 逆序遍历
            for j in range(n, group[i] - 1, -1):
                # 维度2:目前状态的工作获利下限，逆序遍历
                for k in range(minProfit, -1, -1):
                    # todo 注意:如果 k - profit[i-1] 小于零，表示无法达到利润要求，所以我们需要取 max(0, k - profit[i-1])。
                    dp[j][k] += dp[j - group[i]][max(0, k - profit[i])]
                    dp[j][k] % MOD
        # 计算满足要求的方案数,这里不再需要累加求和
        return dp[n][minProfit] % MOD
