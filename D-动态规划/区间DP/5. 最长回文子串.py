"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""

# 方法1：中心扩散法 O(N^2)  推荐！


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 给你一个字符串 s，找到 s 中最长的回文子串。
        
        # todo 返回s[i..j]向两边扩展，可以得到的最长回文串和长度
        def expand(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            # 注意：扩展完之后的i,j都取不到
            return s[i+1:j], j-i

        max_len = 1
        ans = s[0]
        for i in range(len(s)):
            even_s, even_sz = expand(s, i, i+1) # aa，abba类型
            odd_s, odd_sz = expand(s, i-1, i+1) # a, aba类型
            # 取2种类型得到的最大回文串和长度
            if even_sz > max_len:
                max_len = even_sz
                ans = even_s
                
            if odd_sz > max_len:
                max_len = odd_sz
                ans = odd_s

        return ans

# 方法2: dp O(N^2)
# 参考leetcode官方讲解视频, weiwei

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        # 给你一个字符串 s，找到 s 中最长的回文子串。
        n = len(s)
        
        # todo dp[i][j]表示s[i..j]是否是回文串
        # todo 状态转移方程式：dp[i][j] = (s[i]==s[j]) and (j-i+1 <= 3 or dp[i+1][j-1])
        # 也就说dp[i][j]需要参考它在二维矩阵左下方的值
        dp = [[False] * n for _ in range(n)]
        
        # 初始化单字符回文串，可以省略（对角线上的数字不会被参考）
        # for i in range(n):
        #     dp[i][i] = True

        max_len = 1  # 回文子串最大长度
        start = 0    # 最大长度回文串在s中开始索引
        
        # todo 先升序遍历列，再升序遍历行：按照列进行填值
        for j in range(n):
            for i in range(j):  # 只填对角线右上半网格
                sz = j - i + 1
                dp[i][j] = (s[i] == s[j] and (sz <= 3 or dp[i+1][j-1]))

                # 一旦确定s[i..j]是回文串，就更新最大长度
                if dp[i][j] and sz > max_len:
                    max_len = sz
                    start = i

        return s[start: start + max_len]



