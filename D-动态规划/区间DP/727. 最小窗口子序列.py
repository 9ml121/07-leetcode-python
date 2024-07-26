"""
给定字符串 S and T，找出 S 中最短的（连续）子串 W ，使得 T 是 W 的 子序列 。

如果 S 中没有窗口可以包含 T 中的所有字符，返回空字符串 ""。如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。

示例 1：

输入：
S = "abcdebdde", T = "bde"
输出："bcde"
解释：
"bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。
"deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。
 

注：

所有输入的字符串都只包含小写字母。All the strings in the input will only contain lowercase letters.
S 长度的范围为 [1, 20000]。
T 长度的范围为 [1, 100]。
"""
from math import inf

# todo 不定长滑窗 + 正向寻找r, 逆向寻找l(最优解！)
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        # 找s1中最短的连续子串w,使s2是w的子序列
        start = -1
        min_len = inf
        i = 0  # 指向s1
        j = 0  # 指向s2

        # todo 正向遍历s1, 寻找窗口右端点r
        while i < n1:
            if s1[i] == s2[j]:  # s2中的匹配上了，继续匹配s2中的下一个字母
                j += 1

            if j == n2:  
                r = i   # 此时i是符合条件的子数组最右端
                j -= 1  # j复位到s2最后一个元素
                # todo 右端点找到之后，逆向遍历s1[0..i],寻找窗口左端点l
                while j >= 0:
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1  # 此时i是符合条件的子数组最左端
                
                # 更新ans
                cur_len = r-i + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start = i
                    
                # 下一次匹配s2
                j = 0
            i += 1
            
        ans = s1[start: start+min_len] if start != -1 else ''
        return ans


# todo 动态规划：dp代表某个子序列的最小窗口的起点
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        # 找s1中最短的连续子串w,使s2是w的子序列
        min_len = inf
        ans = ''

        # todo dp[i][j]表示s1前i个字符包含s2前j个字符的最近起点, 初始化为-1表示没有匹配上
        # 动态转移：
        # 如果当前s1[i-1]==s2[j-1]，那么这个窗口的起点和dp[i−1][j−1]相同
        # 如果当前字符不相同，因为要包含s2[:j]这个子序列，所以第二维必须是j，即dp[i−1][j]
        dp =  [[-1] * (n2+1) for _ in range(n1+1)]
        # todo 初始化：在第一种情况中，如果dp[i−1][j−1]其中j−1==0，那么起点就是i−1
        for i in range(n1+1):
            dp[i][0] = i
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = dp[i-1][j]
                    
                # 更新ans
                if dp[i][n2] != -1:
                    if i - dp[i][n2] < min_len:
                        ans = s1[dp[i][n2]: i]

        return ans