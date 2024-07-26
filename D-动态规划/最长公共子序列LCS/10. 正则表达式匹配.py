"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


示例 1：
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


提示：

1 <= s.length <= 20
1 <= p.length <= 20
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符


其他示例：
miss iss ippi
mis* is* p*.

   aa b
c* a* b

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        len_s = len(s)
        # dp[i][j] 表示 s 的前 j 个字符与 p 的前 i 个字符是否匹配。
        dp = [[False] * (len_s + 1) for _ in range(len_p + 1)]

        # base case
        # 1.p和 s都为空，true
        dp[0][0] = True

        # 2.p为空，s不为空，fasle

        # 3.p不为空，s为空：需要判断p前i个字符是否连续为’*”
        for i in range(2, len_p + 1):
            if p[i - 1] == '*':
                #  * 匹配前一个字符 0 次
                dp[i][0] = dp[i - 2][0]

        # 状态转移
        for i in range(1, len_p + 1):
            for j in range(1, len_s + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    # 匹配单个字符
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[i - 1] == '*':
                    # * 匹配前一个字符 零次 或 多次
                    dp[i][j] = dp[i - 2][j] or (dp[i][j - 1] and (p[i - 2] == s[j - 1] or p[i - 2] == '.'))

        # print(dp)
        return dp[-1][-1]
