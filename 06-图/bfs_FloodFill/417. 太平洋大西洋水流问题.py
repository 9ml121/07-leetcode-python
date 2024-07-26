"""
有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ，
heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。
水可以从海洋附近的任何单元格流入海洋。

返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。

示例 1：
输入: heights = [[1,2,2,3,5],
                [3,2,3,4,4],
                [2,4,5,3,1],
                [6,7,1,4,5],
                [5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

示例 2：
输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]


提示：
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

"""
import collections
from typing import List


# 方法 1：dfs
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        can_reach_p = [[False] * cols for _ in range(rows)]
        can_reach_a = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            # first col
            can_reach_p[i][0] = True
            # last col
            can_reach_a[i][-1] = True

        for j in range(cols):
            # first row
            can_reach_p[0][j] = True
            # last row
            can_reach_a[-1][j] = True

        def inArea(i, j):
            return 0 <= i < rows and 0 <= j < cols

        # dfs遍历可以流到太平洋的坐标
        def dfs_p(i, j):
            for offsetX, offsetY in offsets:
                newX = i + offsetX
                newY = j + offsetY
                if inArea(newX, newY) \
                        and not can_reach_p[newX][newY] \
                        and heights[i][j] <= heights[newX][newY]:
                    can_reach_p[newX][newY] = True
                    dfs_p(newX, newY)

        # dfs遍历可以流到大西洋的坐标
        def dfs_a(i, j):
            for offsetX, offsetY in offsets:
                newX = i + offsetX
                newY = j + offsetY
                if inArea(newX, newY) \
                        and not can_reach_a[newX][newY] \
                        and heights[i][j] <= heights[newX][newY]:
                    can_reach_a[newX][newY] = True
                    dfs_a(newX, newY)

        for i in range(rows):
            for j in range(cols):
                if can_reach_p[i][j]:
                    dfs_p(i, j)
                if can_reach_a[i][j]:
                    dfs_a(i, j)

        res = []
        for i in range(rows):
            for j in range(cols):
                if can_reach_p[i][j] and can_reach_a[i][j]:
                    res.append([i, j])

        # print(can_reach_p)
        # print(can_reach_a)
        return res


# 方法 2：bfs
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        can_reach_p = [[False] * cols for _ in range(rows)]
        can_reach_a = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            # first col
            can_reach_p[i][0] = True
            # last col
            can_reach_a[i][-1] = True

        for j in range(cols):
            # first row
            can_reach_p[0][j] = True
            # last row
            can_reach_a[-1][j] = True

        def inArea(i, j):
            return 0 <= i < rows and 0 <= j < cols

        # bfs遍历可以流到太平洋的坐标
        def bfs_p(i, j):
            dq = collections.deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for offsetX, offsetY in offsets:
                    newX = x + offsetX
                    newY = y + offsetY
                    if inArea(newX, newY) \
                            and not can_reach_p[newX][newY] \
                            and heights[x][y] <= heights[newX][newY]:
                        can_reach_p[newX][newY] = True
                        dq.append((newX, newY))

        # bfs遍历可以流到大西洋的坐标
        def bfs_a(i, j):
            dq = collections.deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for offsetX, offsetY in offsets:
                    newX = x + offsetX
                    newY = y + offsetY
                    if inArea(newX, newY) \
                            and not can_reach_a[newX][newY] \
                            and heights[x][y] <= heights[newX][newY]:
                        can_reach_a[newX][newY] = True
                        dq.append((newX, newY))

        for i in range(rows):
            for j in range(cols):
                if can_reach_p[i][j]:
                    bfs_p(i, j)
                if can_reach_a[i][j]:
                    bfs_a(i, j)

        res = []
        for i in range(rows):
            for j in range(cols):
                if can_reach_p[i][j] and can_reach_a[i][j]:
                    res.append([i, j])

        # print(can_reach_p)
        # print(can_reach_a)
        return res


if __name__ == '__main__':
    heights1 = [[1, 2, 3],
                [8, 9, 4],
                [7, 6, 5]]
    heights = [[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]
    print(Solution2().pacificAtlantic(heights))
    # [[0,2],[1,0],[1,1],[1,2],[2,0],[2,2]]
    # [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
