"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
    - 插入一个字符
    - 删除一个字符
    - 替换一个字符


示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')


提示：

0 <= word1.n, word2.n <= 500
word1 和 word2 由小写英文字母组成
"""

'''
     0        r             o            s
0   
h                       dp[i-1][j-1]  dp[i-1][j]
o                       dp[i][j-1]    dp[i][j]
r 
s 
e
'''


# todo 解法1：动态规划(推荐！)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 返回将 word1 转换成 word2 所使用的最少操作数
        m, n = len(word1), len(word2)
        
        # dp[i][j] 代表只有word1前i位字符，通过增删改三种方式转换为word2前j位字符，需要的最少步骤
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        

        # base case
        # word2为空,word1[i-1]变word2需删除的操作数
        for i in range(1, m + 1):
            dp[i][0] = i
        # word1为空，word1变word2[j-1]需插入的操作数
        for j in range(1, n + 1):
            dp[0][j] = j
        
        # dp[i][j]状态转移只依赖w1和w2前面一位字符，因此可以依次正序遍历w1,w2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 1.如果word1第i位字符和word2第j位字符一样，最少操作步骤就等于他们各自前一位对应的值
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 2.如果word1第i位字符和word2第j位字符不一样，可以有替换，插入和删除3种操作方式可用
                    # 替换：w1:ab, w2:ac
                    replace = dp[i - 1][j - 1] + 1
                    # 删除：w1:abc, w2:ab
                    delete = dp[i - 1][j] + 1
                    # 插入：w1:ab, w2:abc
                    insert = dp[i][j - 1] + 1
                    # 最终取3种操作最少步骤值
                    dp[i][j] = min(replace, insert, delete)

        # 最少操作步骤就是dp最后一个网格结果
        return dp[-1][-1]


# todo 解法2：深度优先dfs
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import cache
        # 返回将 word1 转换成 word2 所使用的最少操作数
        
        @cache
        def dfs(i=len(word1)-1, j=len(word2)-1):
            # 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            else:
                # ab, ac 替换
                replace = dfs(i - 1, j - 1) + 1  
                # ab, abc 添加
                insert = dfs(i, j - 1) + 1  
                # abc, ac 删除
                delete = dfs(i - 1, j) + 1  # 删除
                return min(replace, insert, delete)
                
        return dfs()


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    Solution().minDistance(word1, word2)
