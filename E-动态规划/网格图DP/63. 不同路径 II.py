"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。



示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1


提示：
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
"""

from typing import List

# todo 动态规划：注意下面状态转移的代码技巧
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 机器人每次只能向下或者向右移动一步。机器人从左上角达到网格的右下角，总共有多少条不同的路径？
        # 网格中的障碍物和空位置分别用 1 和 0 来表示。
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp[i][j]代表从网格左上角到[i,j]位置的路径总数
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            # 第一个位置有障碍物
            return 0
        
        # 初始化
        dp[0][0] = 1

        # 状态转移
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:  # 空位置
                    # todo 当前位置只能由上边，或者左边推导过来, 注意这里代码技巧
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

        # 路径总数就是dp最后一个值
        return dp[-1][-1]

# todo dp空间优化：可以用2个常量来取代dp数组