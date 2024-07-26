"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4


提示：
1 <= k <= nums.n <= 10^5
-10^4 <= nums[i] <= 10^4
"""
import heapq
import random
from typing import List


# todo 方法 2：快速排序，O(n) 没有用到系统栈(推荐！)
# 优化点：1.基准值随机，防止接近有序的极端例子   2.双路快排，防止大量重复元素的用例
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """查找数组中第 K个最大元素"""
        n = len(nums)
        l = 0
        r = n - 1

        # 转换一下：第 k个最大元素，在正序数组索引下标为n - k
        target = n - k

        while l <= r:
            pivotIdx = self.partition(nums, l, r)
            if pivotIdx == target:
                return nums[pivotIdx]
            elif pivotIdx > target:
                r = pivotIdx - 1
            else:
                l = pivotIdx + 1
        
    def partition(self, nums, left, right) -> int:
        """返回pivot在[left..right]闭区间分区之后的索引位置"""
        #  1.基准值随机,或者用中间值
        pivotIdx = random.randint(left, right)
        nums[left], nums[pivotIdx] = nums[pivotIdx], nums[left]
        pivot = nums[left]

        # 2.双指针快排: 重复元素平均分到pivot两边
        le = left + 1
        ge = right
        # nums[left+1..ge) <= pivot
        # nums(ge..right] >= pivot
        while True:
            while le <= ge and nums[le] < pivot:
                le += 1  # le来到第一个大于等于 pivot的位置
            while le <= ge and nums[ge] > pivot:
                ge -= 1  # ge来到第一个小于等于 pivot的位置
            if le > ge:
                break
            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1
        nums[left], nums[ge] = nums[ge], nums[left]
        return ge


'''
# pivot = nums[0] 初始位置 le = 1, ge = 6
# nums[le] < pivot le++ le = 2
size  0 1 2 3 4 5 6 
nums 5 1 5 7 6 5 4
         l       g
# le=2 ge=6  交换元素，然后反向走一步
size  0 1 2 3 4 5 6 
nums 5 1 4 7 6 5 5
           l   g
# le=3 ge=5  交换元素，然后反向走一步
size  0 1 2 3 4 5 6 
nums 5 1 4 5 6 7 5
             lg
# le=4 ge=4  nums[ge] > pivot ge--
size  0 1 2 3 4 5 6 
nums 5 1 4 5 6 7 5
           g l
# 循环打破，交换 left和 ge元素， 返回 ge
size  0 1 2 3 4 5 6 
nums 5 1 4 5 6 7 5
     L     g l
'''

# 方法 1：直接使用排序方法或者堆，时间复杂度都是O(NlogN)
class Solution1:
    # 使用排序方法
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """查找数组中第 K个最大元素: 就是数组逆序排列之后索引为k-1的元素，或者正序排列索引为 n - k 的元素"""
        nums.sort(reverse=True)
        return nums[k - 1]

    # 使用堆排序，时间复杂度：O(NlogK)，遍历数据 O(n)，堆内元素调整 O(logK)；
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """查找数组中第 K个最大元素"""
        return heapq.nlargest(k, nums)[-1]
        # 等价于 return sorted(nums, reverse=True)[k-1]

    # 堆排序的另外写法
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]


if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 5, 7, 6, 5, 4]
    k = 2
    print(s.findKthLargest(nums, k))
    # print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
