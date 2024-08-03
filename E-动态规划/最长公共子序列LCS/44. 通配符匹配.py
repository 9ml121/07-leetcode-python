"""
给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。


示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2：

输入：s = "aa", p = "*"
输出：true
解释：'*' 可以匹配任意字符串。
示例 3：

输入：s = "cb", p = "?a"
输出：false
解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。


提示：

0 <= s.length, p.length <= 2000
s 仅由小写英文字母组成
p 仅由小写英文字母、'?' 或 '*' 组成
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        # # dp[i][j] 表示 s 的前 j 个字符与 p 的前 i 个字符是否匹配。
        dp = [[False] * (len_s + 1) for _ in range(len_p + 1)]

        # base case
        # 1.s和 p都为空
        dp[0][0] = True

        # 2.p为空，s不为空，False

        # 3.p不为空，s为空: 需要判断 p前 i个字符是否为 *
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                # * 匹配 空字符
                dp[i][0] = dp[i - 1][0]

        # 状态转移
        for i in range(1, len_p + 1):
            for j in range(1, len_s + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    # 匹配单个字符
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[i - 1] == '*':
                    # 匹配 空 或者 任意多个字符
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        # print(dp)
        return dp[-1][-1]