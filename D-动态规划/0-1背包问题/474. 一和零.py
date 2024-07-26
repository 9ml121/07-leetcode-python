"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。


提示：
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100
"""
from typing import List

#  todo 01背包问题--装满背包的组合总数
"""
「力扣」第 474 题	                          0-1 背包问题
strs 中的字符串，字符串只能使用一次	          每个物品只能使用一次
每一个字符串或者选入子集，或者不选入子集	    每个物品或者被选入背包或者不选入背包
子集中 最多 有 m 个 0 和 n 个 1	            m 和 n 可以视为背包重量（或者体积）的限制
想让子集中包含的元素最多	                 想让背包中装入的物品价值最大，可以视为每个字符串的「价值」为 1

注意：「子集中 最多 有 m 个 0 和 n 个 1」 区别于 「子集中 恰好 有 m 个 0 和 n 个 1」
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        # dp[i][j][k] 表示：使用字符串数组的前缀区间 [0..i] 里的字符串，并且限制了最多使用 j 个 0 和 k个 1 的最大子集的大小。
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)]

        # 阶段
        for i in range(1, size + 1):
            cnt0 = strs[i - 1].count('0')
            cnt1 = strs[i - 1].count('1')
            # 状态1: '0'的数量
            for j in range(m + 1):  # todo 注意：状态1和2一定是用0开始递增
                # 状态2：'1'的数量
                for k in reversed(range(n + 1)):
                    # 按照「0-1 背包问题」的状态转移过程，先把上一行的值抄下来
                    dp[i][j][k] = dp[i - 1][j][k]
                    # 决策
                    if cnt0 <= j and cnt1 <= k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - cnt0][k - cnt1] + 1)

        # print(dp)
        return dp[size][m][n]


# 空间优化：下标 i 这一行的状态值只参考了下标 i - 1 这一行的状态值，因此可以使用「滚动数组」或者「逆序填表」的方式对使用空间进行优化。
class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[m][n] 表示在前 i 个字符串中，使用 m 个 0 和 n 个 1 能够组成的最大字符串数量。
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            # 注意：这是逆序填表
            for i in reversed(range(zeros, m + 1)):
                for j in reversed(range(ones, n + 1)):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        # print(dp)
        return dp[m][n]
