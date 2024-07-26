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

# todo 方法1：中心扩散法 O(N^2) =》左右双指针
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 找到 s 中最长的回文子串
        n = len(s)
        max_len = 1
        ans = s[0]
        
        def expand(l:int, r:int)-> tuple[str, int]:
            # 以左右指针l,r为中心，向两边扩散验证是否符合回文串性质, 返回最长回文子串和长度元祖
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r], r-l

        # 枚举s每个位置作为回文串中心位置
        for i in range(n):
            # even代表abba类型, odd代表aba类型回文串
            even_s, even_sz = expand(i, i+1)
            odd_s, odd_sz = expand(i-1, i+1)
            
            if even_sz > max_len:
                max_len = even_sz
                ans = even_s
            if odd_sz > max_len:
                max_len = odd_sz
                ans = odd_s
                
        return ans

 # 方法2: 动态规划dp O(N^2)
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j]表示s[i..j]是否是回文串
        dp = [[False] * n for _ in range(n)]
        
        # 初始化单字符符文
        for i in range(n):
            dp[i][i] = True

        max_len = 1
        start = 0
        # 沿矩阵对角线左半边遍历，更新dp[i][j]和ans
        for j in range(n):
            for i in range(j):
                sz = j - i + 1
                dp[i][j] = (s[i] == s[j] and (sz <= 2 or dp[i+1][j-1]))

                if dp[i][j] and sz > max_len:
                    max_len = sz
                    start = i

        return s[start: start + max_len]
