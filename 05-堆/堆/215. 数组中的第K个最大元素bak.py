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

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import heapq
from typing import List


# 方法：优先级队列，堆排序，时间复杂度：O(NlogK)，遍历数据 O(n)，堆内元素调整 O(logK)；
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """查找数组中第 K个最大元素"""
        return heapq.nlargest(k, nums)[-1]
        # 等价于 return sorted(nums, reverse=True)[k-1]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]


if __name__ == '__main__':
    solu = Solution2()
    nums = [3, 2, 1, 5, 6, 4]
    solu.findKthLargest(nums, 2)
