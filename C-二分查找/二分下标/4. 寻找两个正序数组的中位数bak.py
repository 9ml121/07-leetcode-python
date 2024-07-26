"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5




提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


# 方法 1：归并排序，时间复杂度 O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 合并 2 个有序数组
        m, n = len(nums1), len(nums2)
        merge_nums = [0] * (m + n)

        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merge_nums[i + j] = nums1[i]
                i += 1
            else:
                merge_nums[i + j] = nums2[j]
                j += 1
        if i < m:
            merge_nums[i + j:] = nums1[i:]
        if j < n:
            merge_nums[i + j:] = nums2[j:]

        print(merge_nums)
        if (m + n) % 2 == 1:
            return merge_nums[(m + n) // 2]
        else:
            return (merge_nums[(m + n) // 2] + merge_nums[(m + n) // 2 - 1]) / 2


# 方法 2：二分查找，时间复杂度 O(log(m+n))
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 查找 nums1和 nums2这 2 个有序数组组成的数组中第 K大的元素
        def findKthLargest(nums1, start1, len1, nums2, start2, len2, k):
            while True:
                if start1 == len1:
                    return nums2[start2 + k - 1]
                if start2 == len2:
                    return nums1[start1 + k - 1]
                if k == 1:
                    return min(nums1[start1], nums2[start2])

                # 计算中间位置
                mid1 = min(start1 + k // 2 - 1, len1 - 1)
                mid2 = min(start2 + k // 2 - 1, len2 - 1)
                pivot1, pivot2 = nums1[mid1], nums2[mid2]
                if pivot1 <= pivot2:
                    k -= (mid1 - start1 + 1)
                    start1 = mid1 + 1
                else:
                    k -= (mid2 - start2 + 1)
                    start2 = mid2 + 1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        if total_len % 2 == 1:
            mid = total_len // 2 + 1
            return findKthLargest(nums1, 0, m, nums2, 0, n, mid)
        else:
            mid1 = total_len // 2
            mid2 = total_len // 2 + 1
            return (findKthLargest(nums1, 0, m, nums2, 0, n, mid1) + findKthLargest(nums1, 0, m, nums2, 0, n, mid2)) / 2
