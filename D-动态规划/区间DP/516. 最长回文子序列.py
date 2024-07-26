"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。


示例 1：
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

示例 2：
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。


提示：
1 <= s.n <= 1000
s 仅由小写英文字母组成
"""

"""
注意这道题要求的子序列和leetcode第5题要求的子串之间的区别
- 子序列：可以不连续  bbbab => bbbb
- 子串：必须是连续的  bbbab => bbb 或者bab

问题描述：
给定一个字符串 s，找到其中最长的回文子序列的长度。

解题思路：
这道题可以使用动态规划来解决。
1.我们可以定义一个二维数组 dp，其中 dp[i][j] 表示字符串 s 在区间 [i, j] 内的最长回文子序列的长度。
2.首先，我们需要确定动态规划的状态转移方程。对于任意的 i 和 j，
  如果 s[i] 等于 s[j]，那么 dp[i][j] 的值可以通过 dp[i+1][j-1] 加上 2 来得到。
  如果 s[i] 不等于 s[j]，那么 dp[i][j] 的值可以通过 dp[i+1][j] 和 dp[i][j-1] 中的较大值来得到。
具体地：
  如果 s[i] == s[j]，则 dp[i][j] = dp[i+1][j-1] + 2；
  如果 s[i] != s[j]，则 dp[i][j] = max(dp[i+1][j], dp[i][j-1])。

3.接下来，我们需要确定动态规划的计算顺序。
 由于我们需要根据 dp[i+1][j-1]、dp[i+1][j] 和 dp[i][j-1] 来计算 dp[i][j]，所以我们需要保证在计算 dp[i][j] 之前这三个状态已经计算出来。
 因此，我们需要按照从下到上、从左到右的顺序进行计算。
4.最后，dp[0][n-1] 就是我们的答案，其中 n 是字符串 s 的长度。

         a0 b1 c2 b3 b4
    a0   1  1  1  1  3 
    b1   0  1  1  3  3  
    c2   0  0  1  1  2
    b3   0  0  0  1  2 
    b4   0  0  0  0  1
    
    dp[i-1][j]      dp[i][j]
    dp[i+1][j-1]    dp[i+1][j]
    
为了保证每次计算 dp[i][j]正左、正下、左下角方向的位置已经被计算出来，只能斜着遍历或者反着遍历：
"""


# dp遍历方法1：按照左端点i从下往上，右端点j从左往右的顺序遍历（只遍历矩阵斜角右上部分）
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 1.dp[i][j] 代表s[i]开头，s[j]结尾的子串，出现的最长回文子序列长度
        dp = [[0] * n for _ in range(n)]
        # 2.最后返回的结果应该是从i=0开始，到s最后一位j=n-1,即dp[0][n-1]

        # 3.初始化(下面遍历的时候包含了，这步可以省略)
        # 因为s单个字符都代表一个回文，回文子串至少有1个。dp[i][i]就代表子串只有当前s[i]这一个字符，回文长度为1
        # 因为 i 肯定小于等于 j，所以对于那些 i > j 的位置，根本不存在什么子序列，应该初始化为 0。
        # for i in range(n):
        #     dp[i][i] = 1

        # 4.状态转移  abcbb
        # todo 按照左端点i从下往上，右端点j从左往右的顺序遍历（只遍历矩阵斜角右上部分）
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # 如果对应位置字符一样，说明找到了1对回文，
                    # 因为i是倒序遍历，这样dp[i+1][j]的值是确定的
                    # 因为j是正序遍历，这样dp[i][j-1]的值是确定的
                    # 同样，dp[i+1][j-1]的值是确定的
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 如果不相等,取当前值左边和下边的最大值
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                # print(dp)

        return dp[0][n - 1]


if __name__ == '__main__':
    s = 'abcbb'
    print(Solution().longestPalindromeSubseq(s))
