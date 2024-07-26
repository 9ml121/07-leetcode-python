import random
from typing import List

'''
     p
size  0 1 2 3 4 5 6 
nums 2 1 3 2 1 0 4 
       l         g  
# 1 
size  0 1 2 3 4 5 6 
nums 2 1 3 2 1 0 4
         l     g  
# 2 
size  0 1 2 3 4 5 6 
nums 2 1 0 2 1 3 4
           l g 
# 3 
size  0 1 2 3 4 5 6 
nums 2 1 0 1 2 3 4
           g l 
# 4 最后：交换 left和 ge位置元素， 返回 ge
size  0 1 2 3 4 5 6 
nums 1 1 0 2 2 3 4
     L     g l 
'''


# todo 优化 1：基准值选择数组中的随机数，解决数组本身就比较有序的问题
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
        """优化 1：基准值选择数组种的随机数
        """
        randomIdx = random.randint(left, right)
        pivot = nums[randomIdx]
        nums[left], nums[randomIdx] = nums[randomIdx], nums[left]

        j = left
        # all in nums[left + 1..j] <= pivot
        # all in nums(j..i) > pivot
        for i in range(left + 1, right + 1):
            if nums[i] <= pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]

        print(f'j = {j}, nums = {nums}')
        return j


if __name__ == '__main__':
    nums = [5, 0, 1, 4, 2, 6]
    # nums = [5, 2, 3, 1]
    print(nums)
    Solution().sortArray(nums)
    print(nums)
