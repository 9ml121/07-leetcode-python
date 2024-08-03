"""
给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：
对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
请你返回特别排列的总数目，由于答案可能很大，请将它对 10^9 + 7 取余 后返回。

 

示例 1：
输入：nums = [2,3,6]
输出：2
解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。

示例 2：
输入：nums = [1,4,3]
输出：2
解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
 

提示：
2 <= nums.length <= 14
1 <= nums[i] <= 10^9
"""


from functools import cache
from typing import List


# 记忆话搜索：写法 1
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(pre: int = -1, mask: int = 0):
            # pre代表上一个相邻数索引，mask代表已经使用的数字集合二进制压缩状态，1 代表已使用
            if mask == (1 << n) - 1:
                return 1

            res = 0
            for i, x in enumerate(nums):
                if (mask >> i) & 1 == 0 and (pre == -1 or nums[pre] % x == 0 or x % nums[pre] == 0):
                    res += dfs(i, mask | (1 << i))
            return res

        return dfs() % (10**9 + 7)

# 专题1-把X变成Y：写法 2


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        @cache
        def dfs(pre: int, mask: int) -> int:
            # pre代表上一个相邻数索引，mask代表已经使用的数字集合二进制压缩状态，1 代表已使用
            if mask == 0:
                return 1  # 找到一个特别排列

            res = 0
            for j, x in enumerate(nums):
                if mask >> j & 1 and (nums[pre] % x == 0 or x % nums[pre] == 0):
                    res += dfs(j, mask ^ (1 << j))
            return res

        n = len(nums)
        u = (1 << n) - 1
        ans = 0
        for i in range(n):
            ans += dfs(i, u ^ (1 << i))
        return ans % (10**9 + 7)

# 1:1 翻译成递推


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        u = (1 << n) - 1
        # todo 𝑓[𝑆][𝑖] 表示已经排列好的元素（下标）集合为 𝑆，且上一个填的元素（下标）为 𝑖 时，和题目有关的最优值
        f = [[0] * n for _ in range(u)]
        f[0] = [1] * n

        for s in range(1, u):
            for i, pre in enumerate(nums):
                if s >> i & 1:
                    continue
                for j, x in enumerate(nums):
                    if s >> j & 1 and (pre % x == 0 or x % pre == 0):
                        f[s][i] += f[s ^ (1 << j)][j]

        ans = 0
        for i in range(n):
            ans += f[u ^ (1 << i)][i]
        return ans % (10**9 + 7)


# 常规全排列解法：超时
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        used = [False] * n

        def dfs(i: int = 0, pre: int = None) -> int:
            if i == n:
                return 1

            res = 0
            for j in range(n):
                if used[j]:
                    continue

                if i == 0 or (nums[j] % pre) == 0 or pre % nums[j] == 0:
                    used[j] = True
                    res += dfs(i+1, nums[j])
                    used[j] = False

            return res

        return dfs() % (10**9 + 7)

# 测试pycharm  github提交, 解决冲突
