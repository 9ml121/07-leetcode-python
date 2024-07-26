"""
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，
其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，
并且必须在不晚于 lastDayi 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。

示例 1：
输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。

示例 2：
输入：courses = [[1,2]]
输出：1

示例 3：
输入：courses = [[3,2],[4,3]]
输出：0


提示:
1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
"""
import heapq
from typing import List

"""
解题思路：
先说为什么不考虑动态规划。
比如前 3 天上 duration=3 的课程，那么问题就变成从第 4 天开始上课，至多可以上多少课程。
这个思路是没问题，但有亿点点慢。比如在 duration 都比较小，而 lastDay 都比较大的情况下，
上完一门课后，考虑「枚举选哪个」作为接下来要上的课程，我们每次都有 O(n) 个课程可以选，那么总体就需要 O(n^2) 的时间。
在本题的数据范围下，这有可能会超时。

有没有更快的做法呢？来试试贪心行不行。
经验告诉我们，在准备期末考试的时候，先考的课程先准备。
同理，lastDay 越早的课程，应当越早上完。
但是，有的课程 duration 比较长，上完需要花很多时间，可能把这些时间花在其它课程，早就上完好几门课了。

看上去，找不到一个合适的贪心策略。别放弃！顺着这个思路，如果我们可以「反悔」呢？

1.按照 lastDay 从小到大排序，然后遍历 courses。
2.比如先上完 duration=7 的课和 duration=10 的课，后面遍历到了 duration=4 的课，但受到 lastDay 的限制，无法上 duration=4 的课。
3.此时，我们可以「撤销」前面 duration 最长的课，也就是 duration=10 的课，这样就可以上 duration=4 的课了！
4.虽然能上完的课程数目没有变化，但是由于我们多出了 10−4=6 天时间，在后续的遍历中，更有机会上完更多的课程。

在上面的讨论中，我们需要维护一个数据结构，来帮助我们快速找到 duration 最长的课程。
这可以用最大堆解决。
"""


# 贪心算法 + 最大堆（反悔贪心）
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # 按照 lastDay升序排列
        maxHeap = []   # 已学课程的持续时间的最大堆
        cur_time = 0   # 当前日期

        for duration, lastDay in courses:
            # 将持续时间取负值入堆
            heapq.heappush(maxHeap, -duration)  
            cur_time += duration
            # 如果学习当前课程的最后日期超过截止时间，移除最大堆中持续时间最长的课程,并更新当前时间变量
            if cur_time > lastDay:
                max_duration = -heapq.heappop(maxHeap)
                cur_time -= max_duration

        # 返回最大堆的大小，即为最多可以修读的课程数目。
        return len(maxHeap)


if __name__ == '__main__':
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(Solution().scheduleCourse(courses))
