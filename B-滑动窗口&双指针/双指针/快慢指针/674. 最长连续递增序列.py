"""
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1：
输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。

示例 2：
输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。


提示：
1 <= nums.n <= 10^4
-10^9 <= nums[i] <= 10^9
"""
from typing import List

# todo 简单de 快慢双指针 | 动态规划
# 方法1：双指针（推荐！）
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 返回nums最长连续递增子序列长度
        ans = 1
        
        # todo 循环不变量：nums[i..j]严格单调递增
        i = 0
        for j in range(1, len(nums)):
            if nums[j] <= nums[j - 1]:
                # 不符合连续递增，左指针跳到右指针位置
                i = j
                
            ans = max(j - i + 1, ans)
           
        return ans


# 方法2：线性dp
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 返回nums最长连续递增子序列长度
        n = len(nums)
        
        # dp[i]表示nums以i结尾的最长连续递增子序列长度，单个字符长度为1，最后返回结果是max(dp)
        # 动态转移：dp[i]只依赖它前面一个位置结果，nums正序遍历即可
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1

        return max(dp)

    # todo 线性dp压缩为常量
    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        # 返回nums最长连续递增子序列长度
        n = len(nums)

        # dp[i]表示nums以i结尾的最长连续递增子序列长度，单个字符长度为1，最后返回结果是max(dp)
        # 动态转移：dp[i]只依赖它前面一个位置结果，dp数组可以压缩为一个常量
        dp = 1
        ans = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp += 1
                ans = max(ans, dp)
            else:
                dp = 1

        return ans



if __name__ == '__main__':
    cls = Solution()
    nums = [1, 3, 5, 4, 7]
    print(cls.findLengthOfLCIS(nums))
