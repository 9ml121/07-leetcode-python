"""
给你一个大小为 m x n 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (m - 1, n - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为 负数 ，则返回 -1 。

注意，取余是在得到最大积之后执行的。



示例 1：


输入：grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1 。
示例 2：


输入：grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
输出：8
解释：最大非负积对应的路径如图所示 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：


输入：grid = [[1,3],[0,-4]]
输出：0
解释：最大非负积对应的路径如图所示 (1 * 0 * -4 = 0)


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4
"""
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[[1, 1] for _ in range(col)] for _ in range(row)]
        # print(dp)
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        for i in range(1,col):
            dp[0][i][0] = dp[0][i][1] = dp[0][i-1][0] * grid[0][i]
        for i in range(1, row):
            dp[i][0][0] = dp[i][0][1] = dp[i-1][0][0] * grid[i][0]

        for i in range(1, row):
            for j in range(1, col):
                maxProduct = max(dp[i - 1][j][0], dp[i][j - 1][0])
                minProduct = min(dp[i - 1][j][1], dp[i][j - 1][1])
                num = grid[i][j]
                if num < 0:
                    maxProduct, minProduct = minProduct, maxProduct

                maxProduct *= num
                minProduct *= num
                dp[i][j] = [maxProduct, minProduct]

        # print(dp)
        return dp[-1][-1][0] % (10 ** 9 + 7) if dp[-1][-1][0] >= 0 else -1



