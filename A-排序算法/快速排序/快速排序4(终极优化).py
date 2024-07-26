# todo 优化点：
# 1. 基准值：选择数组随机元素，防止分区数据倾斜
# 2. 重复元素：单独分一个区间，在有很多元素和切分元素相等的情况下，递归区间大大减少。
# 3. 小区间使用插入排序
import random
from typing import List


class Solution:
    """三指针快速排序
    """
    # 列表大小等于或小于该大小，将优先于 quickSort 使用插入排序
    def __init__(self, INSERTION_SORT_THRESHOLD=7):
        self.INSERTION_SORT_THRESHOLD = INSERTION_SORT_THRESHOLD

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right) -> None:
        """按照基准值索引位置，将数组切分为 2 部分递归排序
        """
        # todo 小区间使用插入排序
        if right - left <= self.INSERTION_SORT_THRESHOLD:
            self.insertionSort(nums, left, right)
            return

        lt, gt = self.partition(nums, left, right)
        self.quickSort(nums, left, lt - 1)
        self.quickSort(nums, gt + 1, right)

    def partition(self, nums, left, right) -> tuple:
        """三路快排
        """
        randomIdx = random.choice(range(left, right + 1))
        pivot = nums[randomIdx]
        nums[left], nums[randomIdx] = nums[randomIdx], nums[left]

        lt = left + 1  # lt: less than
        gt = right  # ge: greater than
        i = left + 1
        # all in nums[left + 1..lt) < pivot
        # all in nums[lt..i) = pivot
        # all in nums(gt..right] > pivot
        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                i += 1
                lt += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                # nums[i] == pivot
                i += 1

        nums[left], nums[lt - 1] = nums[lt - 1], nums[left]
        return lt - 1, gt

    def insertionSort(self, nums, left, right) -> None:
        """插入排序
        """
        for i in range(left, right + 1):
            j = i
            curr = nums[i]
            # j是从[0..i]向后遍历，目的是把nums[i]插入有序数组nums[0..i-1]
            while j - 1 >= 0 and nums[j - 1] > curr:  # 严格大于
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = curr


if __name__ == '__main__':
    nums = [5, 0, 1, 4, 2, 6]
    # nums = [2, 1, 3, 2, 1, 0, 4]
    # nums = [5, 2, 3, 1]
    print(nums)
    Solution().sortArray(nums)
    print(nums)
