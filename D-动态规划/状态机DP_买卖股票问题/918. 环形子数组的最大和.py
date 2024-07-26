"""
给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。

环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ，
nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，
不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。



示例 1：
输入：nums = [1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

示例 2：
输入：nums = [5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

示例 3：
输入：nums = [3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3


提示：
n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4

"""
from typing import List

# todo 状态dp
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 返回 环形数组 nums 的非空 子数组 的最大可能和
        n = len(nums)
        
        # todo 1.最大子数组不成环：f_max数组统计nums每个位置作为右端点，可以得到的最大子数组和max(f_max)
        # todo 2.最大子数组成环，那么最小子数组就不会成环，f_min数组统计nums每个位置作为右端点，可以得到的最小子数组和, 最大子数组和就是total - min(f_min)
        f_max = [0] * n
        f_max[0] = nums[0]

        f_min = [0] * n
        f_min[0] = nums[0]

        total = nums[0]

        # 把环形数组分成了两个部分
        for i in range(1, n):
            # 1.最大子数组 不成环 , 也就是53题, 取max(f_max)为答案
            f_max[i] = nums[i] + max(f_max[i - 1], 0)
            # 2.最大子数组 成环 ，那么最小子数组就不会成环 --- total - min(f_min) 则为答案
            f_min[i] = nums[i] + min(f_min[i - 1], 0)
            total += nums[i]

        
        if max(f_max) <= 0:
            # 极端情况：数组的所有数都是负数
            return max(f_max)
        else:
            # 取上述2种状态的最大值
            return max(max(f_max), total - min(f_min))


    # todo dp空间优化: 上述2个dp数组状态转移都只依赖前一个位置结果，可以压缩为2个常量(推荐！)
    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        # 返回 环形数组 nums 的非空 子数组 的最大可能和
        total = 0
        maxSum = nums[0]
        minSum = nums[0]
        curMax = 0
        curMin = 0

        for num in nums:
            total += num
            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)

            curMin = min(num, curMin + num)
            minSum = min(minSum, curMin)

        if maxSum <= 0:
            # 极端情况：数组的所有数都是负数
            return maxSum
        else:
            # 取上述2种状态的最大值
            return max(maxSum, total - minSum)
