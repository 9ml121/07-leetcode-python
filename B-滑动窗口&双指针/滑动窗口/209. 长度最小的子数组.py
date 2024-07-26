"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。


示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0


提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


from math import inf
from typing import List

# todo 不固定长度滑动窗口
# 写法1(推荐！)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """返回数组中满足其和 ≥ target 的长度最小的 连续子数组"""
        # 时间复杂度 O(N)
        # 空间复杂度 O(1)
        ans = inf
        
        # 滑动窗口：窗口nums[l..r]内元素和不小于target, 更新ans
        l = 0
        s = 0  # 当前窗口子数组元素和
    
        for r, x in enumerate(nums):
            # 入
            s += x
            
            while s >= target:
                # todo while内部更新ans
                ans = min(ans, r - l + 1)
                # 出
                s -= nums[l]
                l += 1

        # 如果不存在符合条件的子数组，返回 0
        return ans if ans != inf else 0


# 写法2
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """返回数组中满足其和 ≥ target 的长度最小的 连续子数组"""
        ans = float('inf')

        # 滑动窗口：窗口nums[l..r]内元素和不小于target, 更新ans
        l = 0
        s = 0  # 当前子数组的和
        
        for r, x in enumerate(nums):
            # 扩大右窗口
            s += x
            while s - nums[l] >= target:
                s -= nums[l]
            
            if s >= target:
                # todo while外面更新ans
                ans = max(ans, r-l+1)
        
        return ans if ans != float('inf') else 0
