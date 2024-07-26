"""
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。

 

示例 1：



输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
示例 2：



输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
示例 3：


输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。
 

提示：

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""


from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(heights)
        cols = len(heights[0])
        visited = [[False] * cols for _ in range(rows)]

        # dist_to[i][j]代表从原点[0,0]到[i,j]的路径最小绝对值
        dist_to = [[float('inf')] * cols for _ in range(rows)]
        # 最后要求dist_to[-1][-1]

        minHeap = [(0, 0, 0)]  # 路径最大绝对值，横坐标，纵坐标

        while minHeap:
            val1, x1, y1 = heapq.heappop(minHeap)
            cur = heights[x1][y1]
            visited[x1][y1] = True

            for ox, oy in offsets:
                x2 = x1 + ox
                y2 = y1 + oy

                if x2 < 0 or x2 >= rows or y2 < 0 or y2 >= cols:
                    continue

                if visited[x2][y2]:
                    continue

                # 提前到达终点
                if x2 == rows-1 and y2 == cols - 1:
                    return val1

                nxt = heights[x2][y2]
                abs_val = abs(cur - nxt)

                # 贪心
                max_path_val = max(abs_val, val1)
                if max_path_val < dist_to[x2][y2]:
                    dist_to[x2][y2] = max_path_val
                    heapq.heappush(minHeap, (max_path_val, x2, y2))

        return dist_to[-1][-1]
