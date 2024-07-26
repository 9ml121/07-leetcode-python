"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。
如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，
该路径同时满足下述要求：
    - 路径途经的所有单元格的值都是 0 。
    - 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。

畅通路径的长度 是该路径途经的单元格总数。

示例 1：
输入：grid = [[0,1],
             [1,0]]
输出：2

示例 2：
输入：grid = [[0,0,0],
             [1,1,0],
             [1,1,0]]
输出：4

示例 3：
输入：grid = [[1,0,0],
             [1,1,0],
             [1,1,0]]
输出：-1


提示：
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1
"""
import collections
from typing import List


# bfs思路：8个方向
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 1.特判
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        # 8个方向
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dq = collections.deque([(0, 0, 1)])
        visited[0][0] = True

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        minPath = float('inf')
        # dfs遍历所有坐标值为0，并根据是否到达最后一个坐标更新最短路径
        while dq:
            x, y, curPath = dq.popleft()
            if x == rows - 1 and y == cols - 1:
                minPath = min(minPath, curPath)
                continue

            for ox, oy in offsets:
                newX, newY = x + ox, y + oy
                if inArea(newX, newY) and grid[newX][newY] == 0 and not visited[newX][newY]:
                    visited[newX][newY] = True
                    dq.append((newX, newY, curPath + 1))

        return minPath if minPath != float('inf') else -1
