"""
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：
输入：grid = [[0,0,0,0],
             [1,0,1,0],
             [0,1,1,0],
             [0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

示例 2：
输入：grid = [[0,1,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。


提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] 的值为 0 或 1

"""
from typing import List


# 方法 1：dfs
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        can_leave = [[False] * cols for _ in range(rows)]

        def inArea(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j):
            for offsetX, offsetY in offsets:
                newX = i + offsetX
                newY = j + offsetY
                if inArea(newX, newY) \
                        and grid[newX][newY] == 1 \
                        and not can_leave[newX][newY]:
                    can_leave[newX][newY] = True
                    dfs(newX, newY)

        # 先dfs遍历四条边上可以离开的
        for i in range(rows):
            if grid[i][0] == 1:
                can_leave[i][0] = True
                dfs(i, 0)
            if grid[i][-1] == 1:
                can_leave[i][-1] = True
                dfs(i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 1:
                can_leave[0][j] = True
                dfs(0, j)
            if grid[-1][j] == 1:
                can_leave[-1][j] = True
                dfs(rows - 1, j)

        # 再dfs遍历中间不能离开的坐标个数
        cnt = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 1 and not can_leave[i][j]:
                    cnt += 1
        return cnt
