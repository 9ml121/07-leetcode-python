"""
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。

数据范围：区间组数 0≤n≤2×10^5，区间内 的值都满足0≤value≤2×10^5

要求：空间复杂度O(n)，时间复杂度O(nlogn)
进阶：空间复杂度O(value)，时间复杂度O(value)

输入：
    [[10,30],[20,60],[80,100],[150,180]]
返回值：
    [[10,60],[80,100],[150,180]]

输入：
    [[0,10],[10,20]]
返回值：
    [[0,20]]
"""
from typing import List


# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b


# 方法: 排序+贪心(推荐使用)
class Solution:
    def merge(self, intervals: list) -> list:
        mergeRan = []
        # 去除特殊情况
        if len(intervals) == 0:
            return mergeRan

        # 1.按照区间首排序
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        # 2.放入第一个区间
        mergeRan.append(intervals.pop(0))
        # 3.遍历后续区间，查看是否与末尾有重叠
        for interval in intervals:
            s0, e0 = mergeRan[-1]
            si, ei = interval
            # 3.1 区间有重叠，合并后加入
            if si <= e0:
                mergeRan.pop()
                mergeRan.append([s0, max(e0, ei)])
            else:
                mergeRan.append(interval)

        return mergeRan


# 测试

cls = Solution()
# intervals = [[20, 40], [10, 50]]
intervals = [[1, 4], [2, 3]]
# intervals = [[10, 30], [20, 60], [80, 100], [150, 180]]
arr = cls.merge(intervals)
print(arr)
