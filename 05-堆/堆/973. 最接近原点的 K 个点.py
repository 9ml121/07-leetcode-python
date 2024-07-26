"""
给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。

这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。

你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。



示例 1：



输入：points = [[1,3],[-2,2]], k = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], k = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）


提示：

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""
import heapq
import math
import random
from typing import List


# 堆排序
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(math.sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            res.append(list(heapq.heappop(min_heap)[1]))

        return res


"""
除了使用最小堆的解法，还可以使用快速选择算法来解决这个问题。 
 
快速选择算法的思路是选择一个基准点，将点集分为两部分：小于基准点的部分和大于基准点的部分。然后根据基准点的位置，决定继续在哪一部分进行查找。如果基准点的位置恰好是第k个点，那么基准点及其左边的点就是距离最小的k个点。如果基准点的位置大于k，那么继续在左边的部分进行查找；如果基准点的位置小于k，那么继续在右边的部分进行查找。 
 
以下是使用快速选择算法的解法：
"""


# 原地快排
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSelect(points, 0, len(points) - 1, k)
        return points[:k]

    def quickSelect(self, points: List[List[int]], start: int, end: int, k: int) -> None:
        if start >= end:
            return
        pivot = self.partition(points, start, end)
        if pivot == k:
            return
        elif pivot < k:
            self.quickSelect(points, pivot + 1, end, k)
        else:
            self.quickSelect(points, start, pivot - 1, k)

    def partition(self, points: List[List[int]], start: int, end: int) -> int:
        pivot = random.randint(start, end)
        points[start], points[pivot] = points[pivot], points[start]
        pivot = start
        for i in range(start, end):
            if self.compare(points[i], points[end]):
                points[i], points[pivot] = points[pivot], points[i]
                pivot += 1
        points[pivot], points[end] = points[end], points[pivot]
        return pivot

    def compare(self, p1: List[int], p2: List[int]) -> bool:
        return p1[0] ** 2 + p1[1] ** 2 <= p2[0] ** 2 + p2[1] ** 2
