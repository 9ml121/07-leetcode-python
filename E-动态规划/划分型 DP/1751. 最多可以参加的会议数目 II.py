"""
给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在 startDayi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k 表示你能参加的最多会议数目。

你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。

请你返回能得到的会议价值 最大和 。

 

示例 1：

输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
输出：7
解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。
示例 2：



输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
输出：10
解释：参加会议 2 ，得到价值和为 10 。
你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。
示例 3：



输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
输出：9
解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。
 

提示：

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106
"""


from bisect import bisect_left
from typing import List

# todo §6.4 不相交区间
# todo 动态规划 + 二分查找优化
# 相似题目：1235. 规划兼职工作.py
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 按照结束时间排序
        events.sort(key=lambda e: e[1])
        n = len(events)
        # 定义 f[i][j] 表示参加前 i 个会议中的至多 j 个，能得到的会议价值的最大和。
        f = [[0] * (k + 1) for _ in range(n + 1)]

        for i, (start, end, val) in enumerate(events):
            # hi=i 表示二分上界为 i（默认为 n）
            p = bisect_left(events, start, hi=i, key=lambda e: e[1])
            for j in range(1, k + 1):
                # 为什么是 p 不是 p+1：上面算的是 >= start，-1 后得到 < start，但由于还要 +1，抵消了
                f[i + 1][j] = max(f[i][j], f[p][j - 1] + val)
        return f[n][k]

"""
算法小课堂：标准库二分的灵活运用
在写二分题目时，经常会遇到形如「在有序数组中查询大于某个数的最小数」这类问题。具体来说有四类：
    ≥：在有序数组中查询大于或等于某个数的最小数；
    >：在有序数组中查询大于某个数的最小数；
    ≤：在有序数组中查询小于或等于某个数的最大数；
    <：在有序数组中查询小于某个数的最大数。
上面的一些编程语言用到了标准库中的二分，但这些二分在设计的时候，只提供了查询 ≥ 和 > 的功能，并没有提供查询 ≤ 和 < 的功能。

没有关系，稍微转换下就能解决。比如查询 > 得到了下标 i，那么 i−1 就是 ≤ 的结果了（假设数组为升序），同理 < 可以用 ≥ 算出来。

注：> 和 ≥ 也可以转换，对于整数来说，>x 等价于 ≥x+1。



作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
"""