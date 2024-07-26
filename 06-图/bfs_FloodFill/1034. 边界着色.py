"""
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。
网格中的每个值表示该位置处的网格块的颜色。
如果两个方块在任意 4 个方向上相邻，则称它们 相邻 。
如果两个方块具有相同的颜色且相邻，它们则属于同一个 连通分量 。

连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：
1.在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻
2.在网格的边界上（第一行/列或最后一行/列）

请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色。

并返回最终的网格 grid 。

示例 1：
输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]

示例 2：
输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]

示例 3：
输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]


提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n
"""
from typing import List


# dfs方法
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original = grid[row][col]
        visited = [[False] * cols for _ in range(rows)]  # 判断dfs的坐标是否已经访问过
        needChange = [[False] * cols for _ in range(rows)]  # 标记要改变颜色的坐标

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # 判断是够属于连通分量的边界
        def is_inBorder(x, y):
            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                return True
            for offsetX, offsetY in offsets:
                newX, newY = x + offsetX, y + offsetY
                if grid[newX][newY] != original:
                    return True
            return False

        # 判断哪些坐标需要改变颜色
        def dfs(x, y):
            if is_inBorder(x, y):
                needChange[x][y] = True
            visited[x][y] = True

            for offsetX, offsetY in offsets:
                newX, newY = x + offsetX, y + offsetY
                if inArea(newX, newY) \
                        and grid[newX][newY] == original \
                        and not visited[newX][newY]:
                    visited[newX][newY] = True
                    dfs(newX, newY)

        dfs(row, col)
        # 改变原来grid的坐标颜色
        for i in range(rows):
            for j in range(cols):
                if needChange[i][j]:
                    grid[i][j] = color

        # print(grid)
        return grid


if __name__ == '__main__':
    grid = [[1, 2, 2], [2, 3, 2]]  # [[1, 3, 3], [2, 3, 3]]
    row = 0
    col = 1
    color = 3
    print(Solution().colorBorder(grid, row, col, color))

    grid2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    row2 = 1
    col2 = 1
    color2 = 2
    print(Solution().colorBorder(grid2, row2, col2, color2))
