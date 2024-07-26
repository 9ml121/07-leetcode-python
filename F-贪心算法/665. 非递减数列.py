"""
给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。


示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
 

提示：

n == nums.length
1 <= n <= 10^4
-10^5 <= nums[i] <= 10^5
"""

# todo 考虑各种边界情况，贪心改变数组的值
# 贪心性质： 末尾数字越小，对形成递增序列越有利。
class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        # 判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
        n = len(nums)
        change = 0

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                change += 1

                if change > 1:
                    return False

                # todo nums =[3,4,2,3]  nums=[-1,4,2,3]
                # 当nums[2] < nums[0]，这个时候只能修改nums[2]
                # 当nums[2] >= nums[0]，按照贪心性质，只需要修改nums[1]，因为nums[1]对后面判断没有影响了，所以代码上没有必要修改，只是假设 它 已经被修改
                if i >= 2 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]

        return True
