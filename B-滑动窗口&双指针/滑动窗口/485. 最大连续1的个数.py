"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

示例 1：
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

示例 2:
输入：nums = [1,0,1,1,0,1]
输出：2


提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
"""
from typing import List

# todo 简单的不固定长度滑窗
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums最大连续 1 的个数
        ans = 0  
        # 统计每个窗口包含连续1的个数
        cur_ones = 0  
        for num in nums:
            if num == 1:
                cur_ones += 1
                ans = max(ans, cur_ones)
            else:
                cur_ones = 0
        
        return ans
