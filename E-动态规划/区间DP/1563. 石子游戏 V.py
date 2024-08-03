"""
几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。

游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；
Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。
如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。
只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。

返回 Alice 能够获得的最大分数 。

示例 1：
输入：stoneValue = [6,2,3,4,5,5]
输出：18
解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。

示例 2：
输入：stoneValue = [7,7,7,7,7,7,7]
输出：28

示例 3：
输入：stoneValue = [4]
输出：0


提示：
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""
from typing import List


# dp超时
class Solution1:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]
        # dp[i][i] = 0
        for gap in range(1, n):
            for i in range(n - gap):  # j = i + gap < n
                j = i + gap
                for k in range(i, j):
                    left = sum(stoneValue[i:k + 1])
                    right = sum(stoneValue[k + 1:j + 1])
                    if left < right:
                        dp[i][j] = max(dp[i][j], left + dp[i][k])
                    elif left > right:
                        dp[i][j] = max(dp[i][j], right + dp[k + 1][j])
                    else:
                        dp[i][j] = max(dp[i][j], left + dp[i][k], right + dp[k + 1][j])
            # print(dp)
        return dp[0][n - 1]


# dp + 前缀和:超时
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefixSum = [0] * (n + 1)  # 计算前缀和
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + stoneValue[i - 1]
        # dp[i][j] 表示在区间 [i, j] 内进行游戏时，Alice 能够获得的最大分数。
        dp = [[0] * n for _ in range(n)]
        # dp[i][i] = 0
        for gap in range(1, n):
            for i in range(n - gap):  # j = i + gap < n
                j = i + gap  # 结束位置
                for k in range(i, j):  # 枚举分割点
                    left = prefixSum[k + 1] - prefixSum[i]  # 左子区间总价值和
                    right = prefixSum[j + 1] - prefixSum[k + 1]  # 右子区间总价值和
                    if left < right:
                        dp[i][j] = max(dp[i][j], left + dp[i][k])
                    elif left > right:
                        dp[i][j] = max(dp[i][j], right + dp[k + 1][j])
                    else:
                        dp[i][j] = max(dp[i][j], left + dp[i][k], right + dp[k + 1][j])
            # print(dp)
        return dp[0][n - 1]


# dfs + memo
class Solution2:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefixSum = [0] * (n + 1)  # 计算前缀和
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + stoneValue[i - 1]
        memo = [[-1] * n for _ in range(n)]  # 初始化记忆化数组

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            if i == j:
                return 0
            # if i == j - 1:
            #     return min(stoneValue[i], stoneValue[j])
            res = 0
            for k in range(i, j):
                left = prefixSum[k + 1] - prefixSum[i]  # 左子区间总价值和
                right = prefixSum[j + 1] - prefixSum[k + 1]  # 右子区间总价值和
                if left < right:
                    res = max(res, left + dfs(i, k))
                elif left > right:
                    res = max(res, right + dfs(k + 1, j))
                else:
                    res = max(res, left + max(dfs(i, k), dfs(k + 1, j)))
            memo[i][j] = res
            # print(memo)
            return res

        return dfs(0, n - 1)


if __name__ == '__main__':
    stoneValue = [6, 2, 3, 4, 5, 5]
    print(Solution().stoneGameV(stoneValue))
    # print(Solution2().stoneGameV(stoneValue))
