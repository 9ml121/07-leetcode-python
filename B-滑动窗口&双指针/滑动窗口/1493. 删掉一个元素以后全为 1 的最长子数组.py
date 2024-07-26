"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
 

提示：

1 <= nums.length <= 105
nums[i] 要么是 0 要么是 1 。
"""
# todo 简单的不固定长度滑窗
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # nums元素只有0和1，删除nums中一个元素，返回只包含1的最长子数组
        ans = 0

        # [l..r]滑窗内最多包含1个0，zeros代表当前窗口0的个数
        zeros = 0

        l = 0
        for r, x in enumerate(nums):
            # 入
            if x == 0:
                zeros += 1

            # 出
            while zeros > 1:
                zeros -= (nums[l] == 0)
                l += 1

            # 更新ans(注意：必须要删除1个)
            ans = max(ans, r-l)

        return ans
