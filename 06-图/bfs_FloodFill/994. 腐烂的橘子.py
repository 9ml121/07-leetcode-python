"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
    值 0 代表空单元格；
    值 1 代表新鲜橘子；
    值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

示例 1：
输入：grid = [
[2,1,1],
[1,1,0],
[0,1,1]]
输出：4

示例 2：
输入：grid = [
[2,1,1],
[0,1,1],
[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

示例 3：
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
"""
import collections
from typing import List


# 方法1：BFS(需要先遍历一次矩阵，将所有已经腐败的橘子加入队列, 没有用vis数组，直接修改grid值)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1
        m, n = len(grid), len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # todo dq记录bfs遍历遇到的还未访问的腐烂橘子坐标 + 扩散时间
        dq = collections.deque([]) 
        depth = 0  # depth记录队列循环次数，也就是橘子腐烂经过的分钟数
        ones = 0  # ones记录grid还剩下新鲜橘子数据

        # 初始化dq和ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # 值 2 代表腐烂的橘子。
                    dq.append((i, j, depth))
                elif grid[i][j] == 1:  # 值 1 代表新鲜橘子；
                    ones += 1
        # bfs
        while dq:
            x, y, depth = dq.popleft()
            for ox, oy in offsets:
                nx, ny = x + ox, y + oy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # 直接修改值，避免用vis数组
                    dq.append((nx, ny, depth + 1))
                    ones -= 1

        # 队列最后弹出的depth，就是bfs遍历的最大层数，也就是所有橘子都腐烂经过的分钟数
        return depth if ones == 0 else -1


# bfs写法2：queue只记录标记为2的橘子坐标，depth单独统计（比较标准，但写起来麻烦）
def orangesRotting2(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dq = collections.deque([])

    # add the rotten orange to the queue
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                dq.append((i, j))

    # bfs
    depth = 0  # 记录bfs层数，也就是橘子腐烂经过的分钟数
    while dq:
        exist = False  # todo 标记下一层还有没有新鲜的橘子
        size = len(dq)
        for _ in range(size):
            x, y = dq.popleft()
            for ox, oy in offsets:
                newX, newY = x + ox, y + oy
                if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == 1:
                    exist = True
                    grid[newX][newY] = 2
                    dq.append((newX, newY))
        if exist:
            depth += 1

    # if there are still fresh oranges, return -1
    for rows in grid:
        if 1 in rows:
            return -1
    return depth


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(grid))
