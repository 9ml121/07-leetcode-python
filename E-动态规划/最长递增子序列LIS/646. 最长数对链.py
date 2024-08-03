"""
给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。

现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。

找出并返回能够形成的 最长数对链的长度 。

你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。



示例 1：

输入：pairs = [[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4] 。
示例 2：

输入：pairs = [[1,2],[7,8],[4,5]]
输出：3
解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。


提示：

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
"""
from typing import List


# 最优解法：排序 + 贪心  时间复杂度 O(NlogN)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 最少有 1 个数对链
        res = 1
        # 按照 right升序
        pairs.sort(key=(lambda x: x[1]))

        n = len(pairs)
        pre_right = pairs[0][1]
        for i in range(1, n):
            left, right = pairs[i]
            if left > pre_right:
                res += 1
                pre_right = right

        return res


# 方法 2：暴力解法动态规划，时间复杂度 O(N^2)
class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=(lambda x: x[0]))
        n = len(pairs)
        # dp[i] 存储以 pairs[i] 结尾的最长链的长度
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
