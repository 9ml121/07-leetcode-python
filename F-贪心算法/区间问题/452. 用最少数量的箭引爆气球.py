"""
有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，
其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。


示例 1：
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。

示例 2：
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。

示例 3：
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。


提示:
1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1
"""
from typing import List


# todo 方法 1：贪心算法 + 区间相交
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 1.按照 区间右端点 升序排序
        points.sort(key=lambda x: x[1])
        # print(points)  # [[1, 6], [2, 8], [7, 12], [10, 16]]

        n = len(points)
        # 2.pre_end 代表已经看到的不重叠区间，最后一个区间右端点
        #  2.1 如果看到的新区间与前一个区间有重叠，取较小的那个右端点，这样可以保证同一个箭可以射到
        #  2.2 如果没有重叠，更新 pre_end为看到的新区间端点， 同时需要的弓箭数 + 1
        pre_end = points[0][1]
        res = 1
        for i in range(1, n):
            start, end = points[i]
            if start > pre_end:  # 与前一个区间没有重叠
                res += 1
                pre_end = end

        return res


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(Solution().findMinArrowShots(points))
