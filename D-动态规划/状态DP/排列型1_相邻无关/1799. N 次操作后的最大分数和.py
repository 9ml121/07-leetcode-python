"""
给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。

在第 i 次操作时（操作编号从 1 开始），你需要：

选择两个元素 x 和 y 。
获得分数 i * gcd(x, y) 。
将 x 和 y 从 nums 中删除。
请你返回 n 次操作后你能获得的分数和最大为多少。

函数 gcd(x, y) 是 x 和 y 的最大公约数。

 

示例 1：

输入：nums = [1,2]
输出：1
解释：最优操作是：
(1 * gcd(1, 2)) = 1
示例 2：

输入：nums = [3,4,6,8]
输出：11
解释：最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
示例 3：

输入：nums = [1,2,3,4,5,6]
输出：14
解释：最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

提示：

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
"""


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        # 预处理：求 nums任意两个数的gcd
        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        n = len(nums)
        g = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                g[i][j] = gcd(nums[i], nums[j])

        # 状态压缩 + 动态规划
        f = [0] * (1 << n)
        for mask in range(1 << n):
            cnt = mask.bit_count()
            if cnt % 2 == 0:
                for i in range(n):
                    if mask >> i & 1:
                        for j in range(i+1, n):
                            if mask >> j & 1:
                                f[mask] = max(
                                    f[mask], f[mask ^ (1 << i) ^ (1 << j)] + cnt//2 * g[i][j])

        return f[-1]
