"""
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

示例 1:
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。


提示:

1 <= intervals.n <= 10^5
intervals[i].n == 2
-5 * 104 <= starti < endi <= 5 * 10^4
"""
from typing import List


# todo 考察：贪心思维 + 区间相交
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        思路：
        1. 题目问的是需要移除区间intervals的最小数量,使剩下的区间没有重叠
        2. 将intervals按照start值，或者end排序，问题就等价于为找intervals数组不重叠的区间最大数量
        3. 到底是判断intervals[i]最左边的数，还是最右边的数？？这里按照右值升序更好理解
        """
        # 1.intervals按照end升序排序
        intervals.sort(key=lambda x: x[1])
        ends = [intervals[0][1]]  # 记录不重叠的区间，按照end升序压栈
        ans = 0  # 最后要移除的区间

        for i in range(1, len(intervals)):
            left, right = intervals[i]
            topR = ends[-1]
            if left < topR:  # [2, 4] [3, 5]
                # 两区间有相交， 栈顶还是保持右值最小的区间, 也就是总是移除相交区间右值更大的那个
                ans += 1
            else:  # [1, 2] [2,3]算不相连
                # 两区间不相交，将新的区间压入栈顶
                ends.append(right)

        return ans


# 方法 2：动态规划
class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals按照end升序
        intervals.sort(key=(lambda x: x[1]))
        n = len(intervals)
        # dp[i] 代表截止到 interval[0..i]无重叠区间的个数
        # dp[0]默认为1
        dp = [1] * n

        # 从2个开始：
        right = intervals[0][1]  # 默认最右值
        for i in range(1, n):
            # 判断start
            if intervals[i][0] >= right:
                dp[i] = dp[i - 1] + 1
                right = intervals[i][1]
            else:
                dp[i] = dp[i - 1]  # 右值不变
                # right = intervals[i-1][1]

        # 需要移除的区间
        res = n - dp[n - 1]
        return res
