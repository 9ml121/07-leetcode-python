"""
给定两个人的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排 时间段最早 且合适的会议时间。

如果没有满足要求的会议时间，就请返回一个 空数组。

「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。 

题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

 

示例 1：

输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
输出：[60,68]
示例 2：

输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
输出：[]
 

提示：

1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106
"""
from typing import List

# todo 区间相交 + 同向双指针
# 更优写法
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # 返回相交区间范围>=duration的最早时间区间
        # 两个区间数组都按照开始时间升序
        slots1.sort()
        slots2.sort()
        p1 = p2 = 0

        while p1 < len(slots1) and p2 < len(slots2):
            # 找出交集的边界，或者通用的时间段
            intersect_right = min(slots1[p1][1], slots2[p2][1])
            intersect_left = max(slots1[p1][0], slots2[p2][0])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]

            # 始终移动那个结束时间较早的时间段
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []

# 写法2
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # 返回相交区间范围>=duration的最早时间区间
        # 两个区间数组都按照开始时间升序
        slots1.sort(key=lambda x: x[0]) 
        slots2.sort(key=lambda x: x[0])
        m = len(slots1)
        n = len(slots2)

        i = 0  # 指向slots1
        j = 0  # 指向slots2
        while i < m and j < n:
            if slots1[i][1] < slots2[j][0]:
                # 不相交，且slots1[i]先结束，移动slots1
                i += 1
            elif slots1[i][0] > slots2[j][1]:
                # 不相交，且slots2[j]先结束，移动slots2
                j += 1
            else:
                # 相交,先判断相交区间大小是否>=duration
                start = max(slots1[i][0], slots2[j][0])
                end = min(slots1[i][1], slots2[j][1])
                d = end-start  # 注意：区间是左闭右开
                if d >= duration:
                    return [start, start+duration]
                else:
                    # 如果相交区间范围不满足条件，哪边早结束，移动哪边
                    if slots1[i][1] > slots2[j][1]:
                        j += 1
                    elif slots1[i][1] < slots2[j][1]:
                        i += 1
                    else:
                        # 如果同时结束，两边都向后移动一位
                        i += 1
                        j += 1
        return []



