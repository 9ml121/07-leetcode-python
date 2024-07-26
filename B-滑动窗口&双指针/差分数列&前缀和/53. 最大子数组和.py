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
import sys
from math import inf
from typing import List


# todo 方法1：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        n = len(nums)
        
        # f[i]:代表以nums[i]作为右端点可以得到的连续子数组最大和
        f = [0] * n
        f[0] = nums[0]

        # 动态转移：dp[i]只依赖它前面一个位置的结果, 可以进行空间压缩
        for i in range(1, n):
            f[i] = nums[i] + max(f[i - 1], 0)

        # 最后是要求max(dp)
        return max(f)

    # todo dp空间压缩（类似于贪心思想）， 最优解！
    def maxSubArray2(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        ans = nums[0]
        f = 0
        for num in nums:
            f = num + max(f, 0)
            ans = max(ans, f)
        return ans


# 方法 2：前缀和
# 在动态规划解法中，我们通过状态转移方程推导以 nums[i] 结尾的最大子数组和
# 前缀和数组也可以达到相同的效果。
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        n = len(nums)
        
        # 构建前缀数组
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            

        # 以 nums[i] 结尾的最大子数组和就是 preSum[i+1] - min(preSum[0..i])
        # minSum用来维护preSum[0..i]的最小前缀和
        ans = -inf    # 写成nums[0]也可以
        minSum = inf  # 写成0也可以
        for i in range(n):
            minSum = min(minSum, prefix[i])
            ans = max(ans, prefix[i + 1] - minSum)
            
        return ans

    # 前缀和优化
    def maxSubArray2(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        n = len(nums)
        ans = nums[0]
        
        # 以 nums[i] 结尾的最大子数组和就是 sum - min(preSum[0..i])
        # minSum用来维护preSum[0..i]的最小前缀和
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            ans = max(ans, sum - minSum)
            minSum = min(minSum, sum)

        return ans


# 方法3：分治法
# 每次从中间位置把数组分为左右中三部分， 分别求出左右中（这里中是包括中间元素的子序列）最大和。
# 对左右分别深度递归，三者中最大值即为当前最大子序列和。


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        # 找nums具有最大和的连续子数组, 返回其最大和
        def helper(l: int, r: int) -> int:
            if l > r:
                return -sys.maxsize
            
            mid = (l + r) // 2
            left = helper(l, mid - 1)
            right = helper(mid + 1, r)
            
            left_suffix_max_sum = 0
            right_prefix_max_sum = 0
            
            sum = 0
            for i in reversed(range(l, mid)):
                sum += nums[i]
                left_suffix_max_sum = max(left_suffix_max_sum, sum)
                
            sum = 0
            for i in range(mid + 1, r + 1):
                sum += nums[i]
                right_prefix_max_sum = max(right_prefix_max_sum, sum)
                
            cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
            
            return max(cross_max_sum, left, right)
    
        return helper(0, len(nums) - 1)

    

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # 连续子数组 [4,-1,2,1] 的和最大，为 6 。
    print(Solution().maxSubArray2(nums))
