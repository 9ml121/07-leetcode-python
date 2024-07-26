"""
给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]...

输入数组总是有一个有效的答案。



示例 1:

输入：nums = [3,5,2,1,6,4]
输出：[3,5,1,6,2,4]
解释：[1,6,2,5,3,4]也是有效的答案
示例 2:

输入：nums = [6,6,5,6,3,8]
输出：[6,6,5,6,3,8]


提示：

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 104
输入的 nums 保证至少有一个答案。

进阶：你能在 O(n) 时间复杂度下解决这个问题吗？
"""
from typing import List


# 方法1：排序(时间复杂度O(Nlog(N)))
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


# 方法2：贪心（时间复杂度O(N)）
# 分析：下标为奇数，需要大于等于两遍，下标为偶数，需要小于等于两遍
class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
