"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
m == grid.n
n == grid[i].n
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""
import collections
from typing import List


# todo 方法1 广度优先遍历BFS(借助队列实现)
# 技巧：这里是用一个布尔数组记录每个为1的坐标是否被访问过，避免下次重复遍历，也可以直接将遍历到坐标值为1的值，改为0
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量
        ans = 0  # ans记录队列循环次数，也就是独立岛屿数量
        m, n = len(grid), len(grid[0])
      
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = collections.deque()   # dq记录所有标记为1的坐标
        #  vis = [[False] * cols for _ in range(rows)]  # 这里不用布尔数组，直接改grid的值

        for i in range(m):
            for j in range(n):
                # 统计岛个数：每一个新的1代表一个新的岛
                if grid[i][j] == '1':
                    ans += 1
                    dq.append((i, j))
                    grid[i][j] = '0'

                    # 2.BFS：将坐标值为1，四个方向坐标值也为1的坐标值全部改为0
                    while dq:
                        x, y = dq.popleft()
                        for ox, oy in offsets:
                            nx = x + ox
                            ny = y + oy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                dq.append((nx, ny))

        return ans


# 方法 2：DFS(借助编程语言递归栈实现)
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vis = [[False] * cols for _ in range(rows)]

        # 从坐标为 (i, j) 的点开始进行深度优先遍历
        def dfs(x, y):
            # 将4 个方向有连接的 1  坐标全部进行标记
            vis[x][y] = True
            for ox, oy in offsets:
                nx, ny = x + ox, y + oy
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue
                if not vis[nx][ny] and grid[nx][ny] == "1":
                    dfs(nx, ny)

        ans = 0  # 独立岛屿数量
        for i in range(rows):
            for j in range(cols):
                # 如果是岛屿中的一个点，并且没有被访问过，就进行深度优先遍历
                if grid[i][j] == '1' and not vis[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans


# 方法三：并查集(对于这道题ufs比bfs/dfs效率要低一些)
"""
关于连通性问题，并查集也是常用的数据结构。
思路：
并查集中维护连通分量的个数，在遍历的过程中：
- 相邻的陆地（只需要向右看和向下看）合并，只要发生过合并，岛屿的数量就减少 1；
- 在遍历的过程中，同时记录空地的数量；
- 并查集中连通分量的个数 - 空地的个数，就是岛屿数量。
"""

if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]

    print(Solution2().numIslands(grid))
