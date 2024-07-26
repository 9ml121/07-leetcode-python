"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。


示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4


提示:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104
"""
import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """给定一个无重复元素的排序数组和一个目标值，在数组中找到目标值，并返回其索引。
        如果目标值不存在于数组中，返回它将会被按顺序插入的位置
        写法 1：python二分查找bisect.bisect_left()
        """
        # 注意：这里right初始值设置为 len，表示 len 这个下标也有可能是插入元素的位置
        left, right = 0, len(nums)

        # 目标值索引的可能区间[left..len(nums)]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # 首先排除目标值不可能的区间: [0..mid]
                left = mid + 1
            else:
                # 不断缩小 right边界，在[left..mid]查找（前提是 mid向下取整）
                right = mid
        # 程序走到这里 [left, right] 里一定存在插入元素的位置
        # 退出循环的时候一定有 left == right 成立，因此返回 left 或者 right 均可
        return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """写法 2：python二分查找bisect.bisect_left() """
        # 如果这里 right初始值设置为 len(nums)-1, 二分查找之前需要判断数组为空和最后一个元素之后插入的情况
        left, right = 0, len(nums) - 1

        if len(nums) == 0:
            return 0
        if nums[right] < target:
            return right + 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """方法 2：直接调用 bisect"""
        idx = bisect.bisect_left(nums, target)
        # [0..idx-1] < t , [idx..n]>=t
        return idx
