"""
给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。



示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]


提示:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 和 nums2 均为升序排列
1 <= k <= 104
"""
import heapq
from typing import List


# 内存超限
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        minHeap = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(minHeap, (num1 + num2, num1, num2))

        ans = []
        for i in range(min(k, len(minHeap))):
            _, num1, num2 = heapq.heappop(minHeap)
            ans.append([num1, num2])

        return ans


# 每次从堆中弹出一个可以确定的最小值，再加入一个潜在的次小值
class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)

        minHeap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, n1))]  # 最多只维护k个元素

        ans = []
        while minHeap and len(ans) < k:
            _, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < n2:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans
