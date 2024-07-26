""" 
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 
s = "()(())" ==> 6
提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        maxLen = 0
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i-2] + 2
                
                else:
                    # ())  
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        if i-dp[i-1]-2 >= 0:
                            dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
                        else:
                            dp[i] = dp[i-1] + 2
                
                maxLen = max(maxLen, dp[i])
        
        return maxLen

if __name__ == '__main__':
    # s = "()(())"  # 6
    s = "))))((()(("  # 2
    print(Solution().longestValidParentheses(s))