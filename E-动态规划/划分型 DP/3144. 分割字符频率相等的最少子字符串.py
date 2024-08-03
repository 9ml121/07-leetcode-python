"""
给你一个字符串 s ，你需要将它分割成一个或者更多的 平衡 子字符串。比方说，s == "ababcc" 那么 ("abab", "c", "c") ，("ab", "abc", "c") 和 ("ababcc") 都是合法分割，但是 ("a", "bab", "cc") ，("aba", "bc", "c") 和 ("ab", "abcc") 不是，不平衡的子字符串用粗体表示。

请你返回 s 最少 能分割成多少个平衡子字符串。

注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。

 

示例 1：

输入：s = "fabccddg"

输出：3

解释：

我们可以将 s 分割成 3 个子字符串：("fab, "ccdd", "g") 或者 ("fabc", "cd", "dg") 。

示例 2：

输入：s = "abababaccddb"

输出：2

解释：

我们可以将 s 分割成 2 个子字符串：("abab", "abaccddb") 。

 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母。
"""


from collections import defaultdict
from functools import cache
from math import inf

# todo 划分型 DP 固定套路，见 动态规划题单 中的「§6.2 计算划分个数」。
# 方法二：递推（1:1 翻译）
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        # 定义 f[i+1] 表示划分前缀 s[0] 到 s[i] 的最小划分个数
        f = [0] + [inf] * n
        
        for i in range(n):
            # 在倒序枚举 j 的同时，用一个哈希表（或者数组）统计每个字符的出现次数。
            # 如果子串中每个字母的出现次数都相等，那么子串是平衡的。
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                # 子串中有 k 种字母，字母出现次数的最大值为 maxCnt
                # 子串是平衡的，当且仅当子串长度等于 k⋅maxCnt
                if i - j + 1 == len(cnt) * max_cnt:
                    f[i + 1] = min(f[i + 1], f[j] + 1)
                    
        return f[n]


# 方法一：专题1-把X变成Y
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(i: int) -> int:
            # 定义 dfs(i) 表示划分前缀 s[0] 到 s[i] 的最小划分个数
            if i < 0:
                return 0
            
            res = inf
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                # 子串中有 k 种字母，字母出现次数的最大值为 maxCnt
                # 子串是平衡的，当且仅当子串长度等于 k⋅maxCnt。
                if i - j + 1 == len(cnt) * max_cnt:
                    res = min(res, dfs(j - 1) + 1)
            return res
        
        return dfs(len(s) - 1)
