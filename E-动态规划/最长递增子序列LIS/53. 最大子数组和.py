"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。


示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23


提示：
1 <= nums.n <= 10^5
-10^4 <= nums[i] <= 10^4


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
"""
from math import inf
from typing import List


# todo 方法1：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        n = len(nums)
        
        # dp[i]:代表以nums[i]作为右端点可以得到的连续子数组最大和
        dp = [0] * n
        dp[0] = nums[0]

        # 动态转移：dp[i]只依赖它前面一个位置的结果, 可以进行空间压缩
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)

        # 最后是要求max(dp)
        return max(dp)

    # todo dp空间压缩（类似于贪心思想）， 最优解！
    def maxSubArray2(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        ans = nums[0]
        pre = 0
        for num in nums:
            pre = num + max(pre, 0)
            ans = max(ans, pre)
        return ans


# 方法 2：前缀和
# 在动态规划解法中，我们通过状态转移方程推导以 nums[i] 结尾的最大子数组和
# 前缀和数组也可以达到相同的效果。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        n = len(nums)
        
        # 构建前缀数组
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            

        # 以 nums[i] 结尾的最大子数组和就是 preSum[i+1] - min(preSum[0..i])
        # mi用来记录preSum[0..i]的最小前缀和
        ans = -inf
        minV = inf
        for i in range(n):
            minV = min(minV, preSum[i])
            ans = max(ans, preSum[i + 1] - minV)
            
        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # 连续子数组 [4,-1,2,1] 的和最大，为 6 。
    print(Solution().maxSubArray2(nums))
