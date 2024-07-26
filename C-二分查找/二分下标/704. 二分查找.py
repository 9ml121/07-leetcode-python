"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""
import bisect
from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        """查找有序数组目标值 target 在数组中的下标。
        方法 1：调用 bisect框架--写法 1
        'Locate the leftmost value exactly equal to x'
        """
        i = bisect.bisect_left(nums, target)
        # i 的范囥[0..len(nums)]  nums[0..i) < x, nums[i..len(nums)] >= x
        if i != len(nums) and nums[i] == target:
            return i
        else:
            return -1

    def search2(self, nums: List[int], target: int) -> int:
        """方法 1：调用 bisect框架--写法 2
        """
        i = bisect.bisect_right(nums, target)  # 跟下面写法等价
        # i = bisect.bisect(nums, target)
        # i 的范围[0..len(nums)]  nums[0..i-1] <= x, nums[i..len(nums)] >= x
        if i == 0 or nums[i - 1] != target:
            return -1
        else:
            return i - 1

    def search3(self, nums: List[int], target: int) -> int:
        """
        方法2：Python 的内置列表函数index，用于比较和查找元素 target 的位置。
        Python 中的列表  index()  方法的性能与列表的大小和元素的位置有关。
        在最好的情况下，即要查找的元素在列表的第一个位置时， index()  方法的时间复杂度为 O(1)。
        在最坏的情况下，即要查找的元素在列表的最后一个位置或不存在时， index()  方法的时间复杂度为 O(n)，
        其中 n 是列表的大小。
        """
        return nums.index(target) if target in nums else -1

    def search4(self, nums: List[int], target: int) -> int:
        """在有序数组 nums中查找目标值 target 所在的位置下标，不存在返回-1。
        方法3：标准二分查找框架--写法 1：在循环体中找到了元素就直接返回
        时间复杂度：二分查找的时间复杂度是 O(logN)，这里 N 是输入数组的长度；
        """
        left, right = 0, len(nums) - 1
        # 目标元素可能存在在区间 [left, right]
        while left <= right:
            # 下取整,防止整形溢出
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 目标元素可能存在在区间 [mid + 1, right]
                left = mid + 1
            else:
                # 目标元素可能存在在区间 [left, mid - 1]
                right = mid - 1
        return -1

    def search5(self, nums: List[int], target: int) -> int:
        """
        方法3：标准二分查找框架：写法 2：在循环体中排除目标元素一定不存在的区间
        """
        left, right = 0, len(nums) - 1
        # 目标元素可能存在在区间 [left, right]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left, mid]
                right = mid
        # 退出循环条件是 left = right, 返回 left 或者 right 均可
        return left if nums[left] == target else -1