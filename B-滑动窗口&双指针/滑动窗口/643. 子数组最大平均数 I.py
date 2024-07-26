"""
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。

 

示例 1：

输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
示例 2：

输入：nums = [5], k = 1
输出：5.00000
 

提示：

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

from typing import List
# todo 简单的固定长度滑窗

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 返回nums长度为k的连续子数组的最大平均数
        n = len(nums)

        # 循环不变量定义：[l..r) 是长度为 k 的窗口
        # 第一个窗口
        win_sum = sum(nums[:k])
        ans = win_sum
        # 后续窗口
        for r in range(k, n):
            # 一进一出
            win_sum += nums[r] - nums[r-k]
            ans = max(ans, win_sum)

        return ans/k
