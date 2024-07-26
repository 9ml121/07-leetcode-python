"""
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，
封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

示例 1：
输入：grid = [[1,1,1,1,1,1,1,0],
             [1,0,0,0,0,1,1,0],
             [1,0,1,0,1,1,1,0],
             [1,0,0,0,0,1,0,1],
             [1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

示例 2：
输入：grid = [[0,0,1,0,0],
             [0,1,0,1,0],
             [0,1,1,1,0]]
输出：1

示例 3：
输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2


提示：
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from typing import List


# 类似1020.飞地的数量
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * col for _ in range(row)]

        def inArea(i, j):
            return 0 <= i < row and 0 <= j < col

        def dfs(i, j):
            for offsetX, offsetY in offsets:
                newX, newY = i + offsetX, j + offsetY
                if inArea(newX, newY) and grid[newX][newY] == grid[i][j] and not visited[newX][newY]:
                    visited[newX][newY] = True
                    dfs(newX, newY)

        # 1. dfs遍历四条边，标记不是封闭岛屿坐标
        for i in range(row):
            if grid[i][0] == 0 and not visited[i][0]:
                visited[i][0] = True
                dfs(i, 0)
            if grid[i][col - 1] == 0 and not visited[i][col - 1]:
                visited[i][col - 1] = True
                dfs(i, col - 1)

        for j in range(col):
            if grid[0][j] == 0 and not visited[0][j]:
                visited[0][j] = True
                dfs(0, j)
            if grid[row - 1][j] == 0 and not visited[row - 1][j]:
                visited[row - 1][j] = True
                dfs(row - 1, j)
        # print(visited)

        # 2.dfs遍历中心区域,记录封闭岛屿数量
        res = 0
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                    res += 1
                    visited[i][j] = True
                    dfs(i, j)

        return res
