"""
给定两个数组 nums1 和 nums2 ，返回 它们的 交集。
输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

 

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
 

提示：
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""


from typing import List


class Solution:
    # 方法1: 哈希集合
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 返回两个数组的交集
        ans = []
        vis = set(nums1)
        for num in nums2:
            if num in vis:
                ans.append(num)
                vis.remove(num)
        return ans

    # todo 方法2：集合运算
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 返回两个数组的交集
        ans =  set(nums1) & set(nums2)
        return list(ans)
