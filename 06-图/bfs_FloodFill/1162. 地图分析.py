"""
你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地。
请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。
如果网格上只有陆地或者海洋，请返回 -1。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：
(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

示例 1：
输入：grid = [[1,0,1],
             [0,0,0],
             [1,0,1]]
输出：2
解释：
海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。

示例 2：
输入：grid = [[1,0,0],
             [0,0,0],
             [0,0,0]]
输出：4
解释：
海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。


提示：
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 不是 0 就是 1
"""
import collections
from typing import List


# bfs:类似leetcode 994. 腐烂的橘子.py
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """找出海洋单元格(0)离它最近的陆地单元格(1)最远的距离"""
        rows, cols = len(grid), len(grid[0])
        dq = collections.deque()
        visited = [[False] * cols for _ in range(rows)]
        # 1.找出所有的陆地单元格(1),加入队列，并标记为已访问
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    dq.append((i, j))

        # 2.如果网格上只有陆地或者海洋，返回 -1。
        if len(dq) == rows * cols or not dq:
            return -1

        # 3.遍历所有陆地单元格，并将4个方向还未访问的(海洋)单元格加入dq
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # 4.bfs层序遍历dq, 每遍历一层，最远距离+1
        maxDist = -1  # 因为第一层都是陆地，后面加入的才是海洋，所以初始值为-1
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for ox, oy in offsets:
                    newX, newY = x + ox, y + oy
                    if inArea(newX, newY) and not visited[newX][newY]:
                        visited[newX][newY] = True
                        dq.append((newX, newY))
            maxDist += 1
        return maxDist


if __name__ == '__main__':
    grid = [[1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]]
    print(Solution().maxDistance(grid))
