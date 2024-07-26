"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。



示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
     
示例 3：
输入：nums = [1,2,3]
输出：3


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List

# todo 状态dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums是环形数组，不能偷相邻房间，问能够偷窃到的最高金额
        # 分为偷 1 号房屋和不偷 1 号房屋 2 种情况计算最大值，最后再取 2 种情况下的最大值
        def helper(nums:list)->int:
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[:-1]), helper(nums[1:]))


    # dp空间优化
    def rob(self, nums: List[int]) -> int:
        # nums是环形数组，不能偷相邻房间，问能够偷窃到的最高金额
        
        def helper(begin:int, end:int)->int:
            # 计算nums[begin..end)可以获得的最大金额
            f1 = 0
            f2 = 0
            for i in range(begin, end):
                cur = max(f1, f2 + nums[i])
                f2 = f1
                f1 = cur

            # print(pre)
            return f1

        # 由于第一个房间和最后一个房间是相连的，所以需要分别计算[0..n-1)和[1..n)下标区间的最大dp值
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = helper(0, n-1)
        ans2 = helper(1, n)
        return max(ans1, ans2)
