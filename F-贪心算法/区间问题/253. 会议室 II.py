"""
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
返回 所需会议室的最小数量 。

示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2

示例 2：
输入：intervals = [[7,10],[2,4]]
输出：1

提示：
1 <= intervals.length <= 104
0 <= starti < endi <= 106

"""
import heapq
from typing import List

# 方法 1：贪心算法 + 优先队列
"""
1.根据经验，我们 总是希望之前的会议越早结束越好，这是因为 如果一个会议结束得越早，那么后面的会议可以开始且不同时进行的概率就会越大
2.当前问题其实要求我们回答的是 可以同时进行的会议有多少个；
3.可以按照会议的开始时间升序排序，然后我们需要关注每个会议结束的时候，即需要 动态维护 同时进行的会议的结尾的时间，
  并且我们关心会议结束的时间，最合适的数据结构是「优先队列」，需要维护的点是「结束时间最早结束越好」；
4.当一个会议的开始时间 大于等于 在优先队列的队首元素的时候，说明一个会议已经结束，此时需要将它从优先队列中出队，
  注意：这样的过程很可能是重复多次的，请见「参考代码」中的注释
"""


#  1.1 按照开始时间升序排列
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 返回 所需会议室的最小数量 => 可以同时进行的会议有多少个；
        intervals.sort(key=lambda x: x[0])
        # print(intervals)  # [[2, 15], [4, 9], [9, 29], [16, 23], [36, 45]]
        res = 0
        minHeap = []

        for start, end in intervals:
            # 这个过程很可能会弹出很多会议，因此使用 while
            while minHeap and start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
            res = max(res, len(minHeap))

        return res

#  1.2 按照结束时间升序排列
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # print(intervals)  # [[4, 9], [2, 15], [16, 23], [9, 29], [36, 45]]

        res = 1
        pre_ends = [intervals[0][1]]  # pre_ends记录目前最少需要的会议室的结束时间， 单调递增
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < pre_ends[0]:
                res += 1
            else:
                i = 0
                while i + 1 < len(pre_ends) and start >= pre_ends[i + 1]:
                    i += 1
                pre_ends.pop(i)
            pre_ends.append(end)
        return res


if __name__ == '__main__':
    intervals = [[4, 9], [2, 15], [16, 23], [9, 29], [36, 45]]
    Solution().minMeetingRooms(intervals)
