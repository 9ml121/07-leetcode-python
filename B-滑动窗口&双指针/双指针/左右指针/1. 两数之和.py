"""
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]


提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
"""
from typing import List


# 方法1：利用字典存储已遍历的元素:索引
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 字典seen用于存储已访问的数值：索引
        seen = {}  
        for i, val in enumerate(nums):
            complement = target - val  # 计算目标值与当前值的差值
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []


# leetcode167题：167. 两数之和 II - 输入有序数组.py
# todo 排序 + 左右双指针(只针对有序数组有效)
"""
核心思路就是 排序 + 双指针。
1. 先给数组从小到大排序，然后双指针 `lo` 和 `hi` 分别在数组开头和结尾，这样就可以控制 `nums[lo]` 和 `nums[hi]` 这两数之和的大小：
2. 如果你想让它俩的和大一些，就让 `lo++`，如果你想让它俩的和小一些，就让 `hi--`。
"""


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """注意：这里对nums排序之后,元素的原来索引位置就找不到了。这里是找出排序之后的两个元素的索引位置"""
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left, right]
            elif s < target:
                left += 1
            else:
                right -= 1
        return []
