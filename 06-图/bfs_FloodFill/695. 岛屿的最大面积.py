"""
给你一个大小为 m x n 的二进制矩阵 grid 。
岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

示例 1：
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

示例 2：
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] 为 0 或 1
"""
import collections
from typing import List

# todo bfs解法, 类似：F-图论\bfs_FloodFill\200. 岛屿数量.py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 返回 grid 中最大的岛屿面积
        # 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，周围都是0
        ans = 0
        m, n = len(grid), len(grid[0])

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    # 还没有被访问到的1，也就是找到一个新的岛屿
                    vis[i][j] = True
                    curArea = 1  # 当前岛屿面积
                    dq = collections.deque([(i, j)])  # dq保存的是相邻节点为1且没有被访问过的坐标

                    # bfs
                    while dq:
                        x, y = dq.popleft()
                        for ox, oy in offsets:
                            nx, ny = x + ox, y + oy

                            # 不越界，值为1且没有被访问过
                            if (0 <= x < m and 0 <= y < n) and grid[nx][ny] == 1 and not vis[nx][ny]:
                                vis[nx][ny] = True
                                curArea += 1
                                dq.append((nx, ny))

                    # bfs之后更新ans
                    ans = max(ans, curArea)
        return ans

# dfs解法
class Solution2:
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs(x, y):
            nonlocal curArea
            visited[x][y] = True
            for offsetX, offsetY in offsets:
                newX, newY = x + offsetX, y + offsetY
                if inArea(newX, newY) and grid[newX][newY] == 1 and not visited[newX][newY]:
                    curArea += 1
                    dfs(newX, newY)

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    curArea = 1
                    dfs(i, j)
                    maxArea = max(maxArea, curArea)
        return maxArea





if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(Solution().maxAreaOfIsland(grid))
    print(Solution2().maxAreaOfIsland(grid))
