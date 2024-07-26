"""
给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：

left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 的长度要尽可能小。
在完成这样的分组后返回 left 的 长度 。

用例可以保证存在这样的划分方法。

 

示例 1：

输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
示例 2：

输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
 

提示：

2 <= nums.length <= 105
0 <= nums[i] <= 106
可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
"""


from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # 1. 先倒序遍历，记录后面数组最小值
        n = len(nums)
        min_vals = [0] * n
        min_vals[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            min_vals[i] = min(min_vals[i+1], nums[i])

        # print(min_vals)
        # 2.再正序遍历，查找符合条件的最短left
        max_val = 0
        for i in range(n):
            max_val = max(max_val, nums[i])
            # 判断left数组最大值是否小于等于right数组最小值
            if max_val <= min_vals[i+1]:
                # 直接返回left的长度
                return i + 1
