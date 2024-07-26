"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.n <= 3 * 10^4
0 <= nums[i] <= 10^5
"""
from typing import List

# 方法 1：贪心算法
"""
「贪心算法」的直觉：
1.只关注 i + nums[i] 的数值，只要 i+ nums[i]>=len-1 ，就表示从当前位置 i 可以跳到数组的最后一个位置。
  在每一步的迭代中还需满足 前提条件：从之前的步骤可以跳到位置 i。
2.所以本题贪心的地方是 i + nums[i] 的值越大越好。

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0  # 能够跳到的最大位置
        i = 0
        while i <= cover:
            if i + nums[i] >= len(nums) - 1:
                return True
            cover = max(cover, i + nums[i])
            i += 1
        return False


# 另外一种写法
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxReached = 0
        for i in range(n):
            if i > maxReached:
                # 代表i这个位置不能由前面位置跳到
                return False
            
            if i + nums[i] >= n - 1:
                # 由当前位置可以调到最后位置
                return True
            
            # 更新可以调到的最大位置索引
            maxReached = max(maxReached, i + nums[i])