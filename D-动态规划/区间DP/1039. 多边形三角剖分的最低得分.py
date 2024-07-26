"""
你有一个凸的 n 边形，其每个顶点都有一个整数值。
给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，
三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。

返回 多边形进行三角剖分后可以得到的最低分 。


示例 1：
输入：values = [1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。

示例 2：
输入：values = [3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

示例 3：
输入：values = [1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。


提示：
n == values.length
3 <= n <= 50
1 <= values[i] <= 100
"""
from typing import List

"""
解题思路：
这是一个动态规划的问题，可以使用动态规划的思想来解决。下面给出该问题的动态规划解法的思路：
1.创建一个二维数组 dp，其中 dp[i][j] 表示从第 i 个顶点到第 j 个顶点之间的凸多边形的最低得分。
2.使用动态规划的思想，从最小的子问题开始，逐步增加问题的规模，直到解决整个问题。
3.对于任意的子问题 dp[i][j]，我们可以遍历所有可能的分割点 k，计算剖分成三角形 (i, k, j) 的得分，
  即 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])，其中 nums 表示顶点的集合。

最终，dp[0][N-1] 即为剖分后所有三角形得分之和的最小值。
"""


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j]表示以第i个顶点到第j个顶点之间的的凸变形最低得分
        # 最后结果是dp[0][n-1]
        # j - i < 2, dp[i][j]=0
        dp = [[0] * n for _ in range(n)]

        # 先枚举[i..j]长度
        for size in range(3, n + 1):  # size = j-i+1
            # 要保证j < n, i 的最大边界为 size - 1 + i < n, 即 i < n - size + 1
            for i in range(n - size + 1):
                j = size - 1 + i
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])
                    # print(dp)
        return dp[0][n - 1]


if __name__ == '__main__':
    # values = [3, 7, 4, 5]  # 144
    values = [1, 3, 1, 4, 1, 5]  # 13
    print(Solution().minScoreTriangulation(values))
