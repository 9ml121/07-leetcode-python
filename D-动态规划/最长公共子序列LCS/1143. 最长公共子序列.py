"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。



示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。


提示：
1 <= text1.n, text2.n <= 1000
text1 和 text2 仅由小写英文字符组成。
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    n1, n2 = len(text1), len(text2)
    # dp[i][j] 代表text1[i-1]结尾，text2[j-1]结尾，能匹配上的最长公共子序列
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    # 外循环：从text1第一个字符开始遍历
    # 内循环：从text2第一位开始找能否等于text1[i]
    for i in range(1, n1 + 1):  # text1
        for j in range(1, n2 + 1):  # text2
            if text2[j - 1] == text1[i - 1]:
                # 如果查找到单个字符能匹配上的
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 如果字符不相同
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 返回结果:最长子序列就是dp最后一位
    return dp[n1][n2]

























