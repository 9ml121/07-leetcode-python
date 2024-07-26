"""
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

 

示例 1：

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

from typing import List
import collections

# todo 不固定长度滑动窗口 + 计数器
# 类似：A-滑动窗口&双指针\滑动窗口\3. 无重复字符的最长子串.py

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 找nums含有不重复元素，最大的连续子数组之和
        ans = 0    # 代表窗口最大元素总和
        s = 0      # 维护当前窗口元素总和
        num_cnts = collections.Counter()  # 维护当前窗口元素个数

        # todo nums[l..r]不含重复元素
        l = 0
        for r, x in enumerate(nums):
            num_cnts[x] += 1
            s += x
            
            while num_cnts[x] > 1:
                # l右移，直到win[l..r]没有重复元素
                remove = nums[l]
                num_cnts[remove] -= 1
                s -= remove
                l += 1
         
            # 更新结果
            ans = max(ans, s)

        return ans
