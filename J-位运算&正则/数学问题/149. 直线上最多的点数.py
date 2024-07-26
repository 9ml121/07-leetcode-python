"""
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。



示例 1：
输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 2：
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4


提示：
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同
"""
import collections
from typing import List


# 遍历点集，计算每两个点之间的斜率，并统计相同斜率的点的数量
# 考察点：数学，哈希
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 2
        for i in range(n - 1):
            cur_points = 1
            x1, y1 = points[i]
            slopes_cnt = collections.defaultdict(int)

            # 计算其他点与原点的斜率
            for j in range(i + 1, n):
                x2, y2 = points[j]
                slope = float('inf') if x2 == x1 else (y2 - y1) / (x2 - x1)
                slopes_cnt[slope] += 1
            cur_points += max(slopes_cnt.values())
            max_points = max(max_points, cur_points)

        return max_points
