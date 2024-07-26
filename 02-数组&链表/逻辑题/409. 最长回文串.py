"""
给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。

在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

 

示例 1:

输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
示例 2:

输入:s = "a"
输出:1
示例 3：

输入:s = "aaaaaccc"
输出:7
 

提示:

1 <= s.length <= 2000
s 只由小写 和/或 大写英文字母组成
"""


import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 用s中的字符可以构造的最长回文串长度
        # aba aa aaa
        ans = 0      # ans先统计出现2个以上的字符至少可以构成的回文串个数
        odd = False  # 是否有奇数个数的字符，如果有，最后结果要加1(回文串中间可以是单个字符)
        cnts = collections.Counter(s)

        for v in cnts.values():
            ans += v // 2 * 2
            if v % 2 == 1:
                odd = True

        return ans + odd
