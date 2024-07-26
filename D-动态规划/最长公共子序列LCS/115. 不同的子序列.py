"""
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 109 + 7 取模。



示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag


提示：

1 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)

        if len_s < len_t:
            return 0

        dp = [[0] * (len_s + 1) for _ in range(len_t + 1)]
        # base case
        for i in range(len_s + 1):
            dp[0][i] = 1

        for i in range(1, len_t + 1):
            # 剪枝：从 i开始
            for j in range(i, len_s + 1):
                if s[j - 1] == t[i - 1] and dp[i - 1][j - 1] > 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]
