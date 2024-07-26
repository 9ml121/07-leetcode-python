"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]


提示：
0 <= nums.n <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
import bisect
from typing import List


# todo 有序数组: 寻找左侧边界/右侧边界的二分查找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """在排序数组中查找元素的第一个和最后一个位置
        方法 1：实现 bisect二分查找左右边界
        """
        if len(nums) == 0:
            return [-1, -1]

        leftIndex = self.bisectLeft(nums, target)
        if leftIndex == -1:
            return [-1, -1]
        # 能走到这里，一定是数组中存在目标元素
        rightIndex = self.bisectRight(nums, target)
        return [leftIndex, rightIndex]

    # 二分查找目标值左侧边界
    def bisectLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        # 可能的搜索区间[left..right]
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                # mid 以及 mid 的左边一定不是目标元素第 1 次出现的位置
                left = mid + 1
            else:
                # 不断缩小右边界，直到找到目标元素第一次出现的位置(前提：mid是向下取整)
                right = mid
        # 循环退出条件 left=right
        return left if nums[left] == target else -1

    # 二分查找目标值右侧边界
    def bisectRight(self, nums, target):
        left, right = 0, len(nums) - 1
        # 可能的搜索区间[left..right]
        while left < right:
            # 注意：这里一定要向上取整
            mid = (right + left + 1) // 2
            if nums[mid] > target:
                # mid 以及 mid 的右边一定不是目标元素最后一次出现的位置
                right = mid - 1
            else:
                # 不断缩小左边界，直到找到目标元素最后一次出现的位置(前提：mid是向上取整)
                left = mid
        # 循环退出条件 left=right
        return left


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """在排序数组中查找元素的第一个和最后一个位置
        方法 2：调用 bisect模块
        """
        start = bisect.bisect_left(nums, target)
        # [0..start-1] < t, [start..len(nums)]>= t
        end = bisect.bisect_right(nums, target)
        # [0..end-1] <= t, [end..len(nums)] > t
        return [start, end - 1] if start != len(nums) and nums[start] == target else [-1, -1]


if __name__ == '__main__':
    nums = [2, 3, 3]
    t = 3
    print(searchRange(nums, t))
