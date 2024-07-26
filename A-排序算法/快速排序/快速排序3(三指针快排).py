import random
from typing import List

'''
 # init: pivot = 2 ,将 nums[i]和 pivot进行比较
      p
 size  0 1 2 3 4 5 6 7
 nums 2 1 3 2 1 0 4 2
        l           g
        i
 # i=1, nums[i]<pivot, i和 l元素交换，i++, l++ 
 size  0 1 2 3 4 5 6 7
 nums 2 1 3 2 1 0 4 2
          l         g
          i
 # i=2, nums[i]>pivot, i和 g元素交换，g--
 size  0 1 2 3 4 5 6 7
 nums 2 1 2 2 1 0 4 3
          l       g
          i
 # i=2, nums[i]==pivot, i++
 size  0 1 2 3 4 5 6 7
 nums 2 1 2 2 1 0 4 3
          l       g
            i
 # i=3, nums[i]==pivot, i++
 size  0 1 2 3 4 5 6 7
 nums 2 1 2 2 1 0 4 3
          l       g
              i
 # i=4, nums[i]<pivot, i和 l元素交换，i++, l++ 
 size  0 1 2 3 4 5 6 7
 nums 2 1 1 2 2 0 4 3
            l     g
                i
 # i=5, nums[i]<pivot, i和 l元素交换，i++, l++ 
 size  0 1 2 3 4 5 6 7
 nums 2 1 1 0 2 2 4 3
              l   g
                  i
# i=6, nums[i]>pivot, i和 g元素交换，g--
 size  0 1 2 3 4 5 6 7
 nums 2 1 1 0 2 2 4 3
              l g
                  i
# 此时 i>gt, 循环条件打破，交换left和 l-1的元素
 size  0 1 2 3 4 5 6 7
 nums 0 1 1 2 2 2 4 3
              l g
                  i
partition函数返回 lt-1, gt
 '''


# todo 优化 3：三指针快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right) -> None:
        """按照基准值索引位置，将数组切分为 2 部分递归排序
        """
        if left >= right:
            return

        lt, gt = self.partition(nums, left, right)
        self.quickSort(nums, left, lt - 1)
        self.quickSort(nums, gt + 1, right)

    def partition(self, nums, left, right) -> tuple:
        """优化 3：把等于切分元素的所有元素挤到了数组的中间，在有很多元素和切分元素相等的情况下，递归区间大大减少。
        """
        randomIdx = random.randint(left, right)
        # randomIdx = left
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


if __name__ == '__main__':
    # nums = [5, 0, 1, 4, 2, 6]
    nums = [2, 1, 3, 2, 1, 0, 4]
    # nums = [5, 2, 3, 1]
    print(nums)
    Solution().sortArray(nums)
    print(nums)
