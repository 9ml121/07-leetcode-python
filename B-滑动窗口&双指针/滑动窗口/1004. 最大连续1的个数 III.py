"""
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

示例 1：
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。


提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1
0 <= k <= nums.length
"""
from typing import List

# todo 不固定长度滑动窗口
# 487. 最大连续1的个数 II.py

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # nums只有0,1；最多可以翻转k个0， 返回 数组中连续 1 的最大个数
        ans = 0
        # todo 滑窗[l..r]最多k个0, zero记录窗口0的个数，超出k需要左移指针​
        zero = 0
        l = 0
        
        for r, num in enumerate(nums):
            # 入
            if num == 0:
                zero += 1

            # 出
            while zero > k:  
                if nums[l] == 0:
                    zero -= 1
                l += 1

            # 更新ans
            ans = max(ans, r - l + 1)

        return ans
