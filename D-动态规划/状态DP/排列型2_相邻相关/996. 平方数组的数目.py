"""
如果一个数组的任意两个相邻元素之和都是 完全平方数 ，则该数组称为 平方数组 。

给定一个整数数组 nums，返回所有属于 平方数组 的 nums 的排列数量。

如果存在某个索引 i 使得 perm1[i] != perm2[i]，则认为两个排列 perm1 和 perm2 不同。

 

示例 1：

输入：nums = [1,17,8]
输出：2
解释：[1,8,17] 和 [17,8,1] 是有效的排列。
示例 2：

输入：nums = [2,2,2]
输出：1
 

提示：

1 <= nums.length <= 12
0 <= nums[i] <= 109
"""


from functools import cache
from typing import List

# 常规全排列：写法 1


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def check(x: int, y: int) -> bool:
            return int((x+y) ** 0.5) ** 2 == (x+y)

        nums.sort()
        n = len(nums)
        used = [False] * n

        def dfs(i: int = 0, pre: int = None):
            if i == n:
                return 1

            res = 0
            for j in range(n):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue

                if i == 0 or check(pre, nums[j]):
                    used[j] = True
                    res += dfs(i+1, nums[j])
                    used[j] = False
            return res

        return dfs()


# todo 排列型 ② 相邻相关:
# 一般定义 𝑓[𝑆][𝑖] 表示已经排列好的元素（下标）集合为 𝑆，且上一个填的元素（下标）为 𝑖 时，和题目有关的最优值。
# f = [[0] * n for _ in range(1 << n)]
# 通过枚举当前位置要填的元素来转移
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # 判断两个数之和是否为完全平方数
        def check(x: int, y: int) -> bool:
            return int((x+y) ** 0.5) ** 2 == (x+y)

        # 排序，方便 dfs去重
        nums.sort()
        n = len(nums)

        @cache
        def dfs(pre: int = -1, mask: int = 0):
            if mask == (1 << n) - 1:
                return 1

            res = 0
            for i in range(n):
                # 去重
                if i > 0 and nums[i] == nums[i-1] and not (mask >> (i-1) & 1):
                    continue

                if (mask >> i) & 1 == 0 and (pre == -1 or check(nums[pre], nums[i])):
                    res += dfs(i, mask | (1 << i))
            return res

        return dfs()
