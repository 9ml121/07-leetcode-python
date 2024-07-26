import random
from typing import List


# todo 优化 2：双指针快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right) -> None:
        """按照基准值索引位置，将数组切分为 2 部分递归排序
        """
        if left >= right:
            return

        pivotIdx = self.partition(nums, left, right)
        self.quickSort(nums, left, pivotIdx - 1)
        self.quickSort(nums, pivotIdx + 1, right)

    def partition(self, nums, left, right) -> int:
        """优化 2：把等于切分元素的所有元素 等概率 地分到了数组的两侧，避免了递归树倾斜，递归树相对平衡；
        """
        randomIdx = random.randint(left, right)
        # randomIdx = left
        pivot = nums[randomIdx]
        nums[left], nums[randomIdx] = nums[randomIdx], nums[left]

        le = left + 1  # le: less equals
        ge = right  # ge: greater equals
        # all in nums[left + 1..le) <= pivot
        # all in nums(ge..right] >= pivot
        while True:
            while le <= ge and nums[le] < pivot:
                le += 1
                # 此时 le来到第一个大余等于 pivot的位置
            while le <= ge and nums[ge] > pivot:
                ge -= 1
                # 此时 ge来到第一个小于等于 pivot的位置
            if le >= ge:
                break
            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1

        nums[left], nums[ge] = nums[ge], nums[left]
        return ge


# partiton函数写法 2
def partition(nums, left, right):
    pivot = nums[left]  # 初始化一个待比较数据
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
            j -= 1
        nums[i] = nums[j]  # 将更小的数放入左边
        while i < j and nums[i] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
            i += 1
        nums[j] = nums[i]  # 将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot  # 待比较数据放入最终位置
    return i  # 返回待比较数据最终位置


if __name__ == '__main__':
    # nums = [5, 0, 1, 4, 2, 6]
    nums = [2, 1, 3, 2, 1, 0, 4]
    # nums = [5, 2, 3, 1]
    print(nums)
    Solution().sortArray(nums)
    print(nums)
