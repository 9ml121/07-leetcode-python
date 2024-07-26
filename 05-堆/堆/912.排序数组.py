"""
leetcode912题：排序数组
给你一个整数数组 nums，请你将该数组升序排列。



示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
import heapq
from typing import List


# 方法1：调用python最小堆模块heapq，完成最小堆升序排序
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)

    def heapSort(self, nums):
        # 注意：这是非原地排序，时间复杂度O(NlogN)）
        heapq.heapify(nums)
        ans = []
        while nums:
            ans.append(heapq.heappop(nums))
        return ans


# 方法2：自己实现原地最大堆排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 「力扣」第 912 题：排序数组
        # 第 1 步：先将nums整理成最大堆
        heapify(nums)
        # 第 2 步：先交换，再将堆顶元素下沉
        # 注意：这里 i 表示当前二叉树所表示的数组的结尾下标
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            _sink(nums, i - 1,  0)
        return nums


def _sink(nums, endPos, pos):
    # endPos ：数组 nums 的尾索引，
    # pos: 要下沉的第一个索引
    # _sink 方法维持 nums[0:end]，包括 nums[end] 在内堆有序
    temp = nums[pos]
    while 2 * pos + 1 <= endPos:
        # 只要有孩子结点：有左孩子，就要孩子结点
        childPos = 2 * pos + 1
        if childPos + 1 <= endPos and nums[childPos] < nums[childPos + 1]:
            # 如果有右边的结点，并且右结点还比左结点大
            childPos += 1
        if nums[childPos] <= temp:
            break
        nums[pos] = nums[childPos]
        pos = childPos
    nums[pos] = temp


def heapify(nums) -> None:
    # 将数组原地转换为最大堆
    size = len(nums)
    for i in range((size - 1) // 2, -1, -1):
        _sink(nums, i, 0)


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    print(Solution().sortArray(nums))
