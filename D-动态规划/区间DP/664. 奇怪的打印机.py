"""
有台奇怪的打印机有以下两个特殊要求：
1.打印机每次只能打印由 同一个字符 组成的序列。
2.每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。

给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

示例 1：
输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。

示例 2：
输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。

提示：
1 <= s.length <= 100
s 由小写英文字母组成
"""

"""
解题思路：
这是一个动态规划的问题，可以使用动态规划的思想来解决。下面给出该问题的动态规划解法的思路：
1.创建一个二维数组 dp，其中 dp[i][j] 表示打印出字符串 s 的区间 [i, j] 需要的最少操作次数。
2.使用动态规划的思想，从最小的子问题开始，逐步增加问题的规模，直到解决整个问题。
3.对于任意的子问题 dp[i][j]，我们可以遍历区间内的所有分割点 k，将区间 [i, j] 分割为两部分 [i, k] 和 [k+1, j]。
  1) 如果 s[k] == s[j]，说明字符 s[j] 可以与前面的某个字符一起打印，因此 dp[i][j] = dp[i][k] + dp[k+1][j-1]；
  2) 否则，我们需要单独打印字符 s[j]，因此 dp[i][j] = dp[i][j-1] + 1。
4.遍历顺序为从字符串的末尾开始向前遍历，从左往右遍历区间长度。
5.最终，dp[0][n-1] 即为打印出整个字符串 s 的最少操作次数，其中 n 是字符串 s 的长度。
"""


# 遍历方法1：
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # 1.dp[i][j] 表示打印出字符串 s 的区间 [i, j] 需要的最少操作次数
        dp = [[0] * n for _ in range(n)]
        # 2.初始化dp[i][i]=1, 最后要算的是dp[0][n-1]
        # 3.动态转移：
        #   1）s[i] == s[j]:  dp[i][j] = dp[i][j - 1]
        #   2）s[i] != s[j]:  dp[i][j] = dp[i][j-1] + 1
        #                     dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j-1])  (k = [i..j), s[k] == s[j])
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + 1
                    for k in range(i, j):
                        if s[k] == s[j]:
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
            print(dp)
        return dp[0][n - 1]


# dp遍历方法2(更好理解, 但是性能比方法1慢一些)
class Solution2:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # 1.dp[i][j] 表示打印出字符串 s 的区间 [i, j] 需要的最少操作次数
        dp = [[0] * n for _ in range(n)]
        # 2.初始化dp[i][i]=1, 最后要算的是dp[0][n-1]
        # 3.动态转移：
        #   1) dp[i][j] = dp[i][j-1] + 1   (s[i] == s[j])
        #   2) dp[i][j] = dp[i][k] + dp[k + 1][j]  (s[i] != s[j])
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
            print(dp)
        return dp[0][n - 1]


if __name__ == '__main__':
    # s = "abcabc"  # 5
    # s = "abba"  # 2
    # s = "aaabbb"  # 2
    s = "abb"  # 2
    print(Solution().strangePrinter(s))
