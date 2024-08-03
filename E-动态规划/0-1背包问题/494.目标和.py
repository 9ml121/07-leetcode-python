"""
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.n <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from functools import cache
from typing import List

# todo 01背包问题--装满背包的组合总数
"""
#  0 <= nums[i] <= 1000
# nums种每个正整数数可以代表正数，也可以代表负数。
# 假设所有代表正数的和为pos, 所有代表负数的和为neg
# pos + neg = sum(nums)
# pos - neg = target
# sum(nums)和target都是已知，问题就转换为求nums数组中可以取出多少个数，其和等于(sum(nums) + target) /2
# 转换为01背包问题，就是有一个容量为w的背包，有len(nums)个物品，问有多少种方式可以装满背包？

「力扣」第 494 题	                            0-1 背包问题
每个数必须选，分为「选正数」和「选负数」	        每个数选与不选
约束条件：所有数的和恰好为 (sum + target) / 2	  约束条件：所有物品的重量 恰好 填满背包的最大承重
目标求所有方案数，每一次状态转移的时候需要累加	     目标求所有物品的价值总和最大，状态转移的时候求最大值
"""


# todo 方法 1：递归搜索 + 保存计算结果 = 专题1-把X变成Y
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) + target
        if s < 0 or s % 2:
            return 0
        m = s // 2  # 背包容量

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)  # 只能不选
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])  # 不选 + 选
        return dfs(len(nums) - 1, m)


# todo 1:1 翻译成递推
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0
        m = s // 2  # 背包容量

        n = len(nums)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(m + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]  # 只能不选
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]  # 不选 + 选
        return f[n][m]

if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]  # 5
    # target = 3
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]  # 256
    target = 1
    print(Solution().findTargetSumWays(nums, target))

    '''
    [[1, 0], [2, 0], [4, 0], [8, 0], [16, 0], [32, 0], [64, 0], [128, 0], [256, 0], [256, 256]]
    '''
