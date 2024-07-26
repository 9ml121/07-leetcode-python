"""
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

 

示例 1：

输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
示例 2：

输入：nums = [1,1,1]
输出：0
 

提示：

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
答案保证符合 32-bit 整数
"""



from typing import List
# todo 数学问题

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # n个数字，让n-1个数字增加1，使所有数字都相等，问这个最小操作次数？
        # 问题等价于：每次让1个数字减少1，使所有数字都相等，最后这个相等的数字一定是nums中的最小数

        min_v = min(nums)
        ans = sum((x-min_v) for x in nums)
        return ans
