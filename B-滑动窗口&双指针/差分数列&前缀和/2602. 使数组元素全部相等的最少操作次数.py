"""
给你一个正整数数组 nums 。

同时给你一个长度为 m 的整数数组 queries 。第 i 个查询中，你需要将 nums 中所有元素变成 queries[i] 。你可以执行以下操作 任意 次：

将数组里一个元素 增大 或者 减小 1 。
请你返回一个长度为 m 的数组 answer ，其中 answer[i]是将 nums 中所有元素变成 queries[i] 的 最少 操作次数。

注意，每次查询后，数组变回最开始的值。

 

示例 1：

输入：nums = [3,1,6,8], queries = [1,5]
输出：[14,10]
解释：第一个查询，我们可以执行以下操作：
- 将 nums[0] 减小 2 次，nums = [1,1,6,8] 。
- 将 nums[2] 减小 5 次，nums = [1,1,1,8] 。
- 将 nums[3] 减小 7 次，nums = [1,1,1,1] 。
第一个查询的总操作次数为 2 + 5 + 7 = 14 。
第二个查询，我们可以执行以下操作：
- 将 nums[0] 增大 2 次，nums = [5,1,6,8] 。
- 将 nums[1] 增大 4 次，nums = [5,5,6,8] 。
- 将 nums[2] 减小 1 次，nums = [5,5,5,8] 。
- 将 nums[3] 减小 3 次，nums = [5,5,5,5] 。
第二个查询的总操作次数为 2 + 4 + 1 + 3 = 10 。
示例 2：

输入：nums = [2,9,6,3], queries = [10]
输出：[20]
解释：我们可以将数组中所有元素都增大到 10 ，总操作次数为 8 + 1 + 4 + 7 = 20 。
 

提示：

n == nums.length
m == queries.length
1 <= n, m <= 105
1 <= nums[i], queries[i] <= 109
"""


import bisect
from typing import List

# todo 排序+前缀和+二分查找


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # 将 nums 中所有元素变成 queries[i] 的 最少 操作次数。
        # 1.排序
        nums.sort()
        n = len(nums)

        # 2.前缀和 s
        s = [0] * (n+1)
        for i, x in enumerate(nums):
            s[i+1] = s[i] + x
        # s = list(accumulate(nums, initial=0))  # 前缀和更简洁写法

        ans = []
        for x in queries:
            # 3.二分查找
            j = bisect.bisect_left(nums, x)
            # nums[0..j] < x
            left = x * j - s[j]   # 蓝色面积
            right = (s[n] - s[j]) - x * (n-j)  # 绿色面积
            ans.append(left+right)

        return ans
