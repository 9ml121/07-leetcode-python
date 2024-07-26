"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""


from typing import List

# 方法 1：模拟法，调用数组的 insert和pop方法
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

# 方法 2：三次旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        Do not return anything, modify nums in-place instead.
        """
        # 首尾交换法
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        # 三次旋转数组
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

# 三次旋转，写法 2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[::] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
