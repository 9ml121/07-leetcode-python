"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

 

示例 1：

输入：nums = [8,2,4,7], limit = 4
输出：2 
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4. 
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4. 
因此，满足题意的最长子数组的长度为 2 。
示例 2：

输入：nums = [10,1,2,4,7,2], limit = 5
输出：4 
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
示例 3：

输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""

import collections
from typing import List

# todo 不固定长度滑窗 + 单调队列/有序列表/堆

# 方法1：不固定长度滑窗 + 2个单调队列（推荐！！）
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 返回nums最长连续数组长度,满足窗口内最大值和最小值的绝对差<=limit
        ans = 0

        min_dq = collections.deque()
        max_dq = collections.deque()

        # todo 循环不变量：nums[l..r]内最大值和最小值的绝对差<=limit
        l = 0
        for r, x in enumerate(nums):
            # 1.入
            while min_dq and x < min_dq[-1]:
                # 维护min_dq单调递增
                min_dq.pop()

            while max_dq and x > max_dq[-1]:
                # 维护max_dq单调递减
                max_dq.pop()

            min_dq.append(x)
            max_dq.append(x)

            # 2.出
            while min_dq and max_dq[0] - min_dq[0] > limit:
                # 窗口左边界右移
                if nums[l] == min_dq[0]:
                    min_dq.popleft()

                elif nums[l] == max_dq[0]:
                    max_dq.popleft()

                l += 1

            # 3.更新ans
            ans = max(ans, r-l+1)

        return ans

# 方法2：滑动窗口 + 2个堆（不推荐，性能比不上dq）
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from heapq import heappop, heappush
        # 返回nums最长连续数组长度,满足窗口内最大值和最小值的绝对差<=limit
        ans = 0
        
        max_ = []  # 大根堆 max_, 保存(值, 索引)
        min_ = []  # 小根堆 min_, 保存(值, 索引)
        
        l = 0
        for r, num in enumerate(nums):
            # 1.入
            heappush(max_, [-num, r])
            heappush(min_, [num, r])
            
            # 2.出
            while -max_[0][0] - min_[0][0] > limit:
                # todo 条件判断需要max,min[0][0]存的索引不在 l 左侧
                # 删除不在 l 右侧的元素
                while min_[0][1] <= l:
                    heappop(min_)
                while max_[0][1] <= l:
                    heappop(max_)
                # 移动 l
                l += 1
                
            # 找到最长的符合要求的窗口长度
            ans = max(ans, r-l+1)
            
        return ans

# 方法3：滑动窗口 + python有序列表SortedList
"""
如果遍历求滑动窗口内的最大值和最小值，时间复杂度是 O(k)，肯定会超时。
降低时间复杂度的一个绝招就是增加空间复杂度：利用更好的数据结构。

为了方便统计当前窗口内的最大值与最小值，我们可以使用平衡树(内部是有序的数据结构)：
1.语言自带的红黑树，例如 C++ 中的 std::multiset, Java 中的 TreeMap；
2.第三方的平衡树库，例如 Python 中的 sortedcontainers（事实上，这个库的底层实现并不是平衡树，但各种操作的时间复杂度仍然很优秀）；
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 返回nums最长连续数组长度,满足窗口内最大值和最小值的绝对差<=limit
        # todo sortedcontainers不是python自带包，需要pip导入
        from sortedcontainers import SortedList 
        
        # 返回nums最长连续数组长度,满足窗口内最大值和最小值的绝对差<=limit
        ans = 0
        # todo 有序列表SortedList用来维护窗口元素有序，方便O(1)时间查找窗口最大值和最小值
        sorted_list = SortedList()
        
        l = 0
        for r, x in enumerate(nums):
            # 1.入
            sorted_list.add(x)
            
            # 2.出
            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[l])
                l += 1
            
            # 3.更新ans
            ans = max(ans, r - l + 1)
        
        return ans
