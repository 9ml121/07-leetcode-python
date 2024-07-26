"""
给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目。

示例 1：
输入：S = "havefunonleetcode", K = 5
输出：6
解释：
这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。

示例 2：
输入：S = "home", K = 5
输出：0
解释：
注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。


提示：
1 <= S.length <= 10^4
S 中的所有字符均为小写英文字母
1 <= K <= 10^4
"""

import collections

# todo 固定长度滑窗 + 计数器

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # 找出所有长度为 K 且不含重复字符的子串，返回全部满足要求的子串的 数目
        ans = 0
        # todo [l..r]滑窗内不含重复字符，且窗口长度<=k; 计数器用来维护窗口内元素个数
        win_cnts = collections.Counter()

        l = 0
        for r, c in enumerate(s):
            # 入
            win_cnts[c] += 1

            # 出
            while win_cnts[c] > 1:
                win_cnts[s[l]] -= 1
                l += 1
            
            if r-l+1 > k:
                win_cnts[s[l]] -= 1
                l += 1

            # 更新ans
            if r-l+1 == k:
                ans += 1

        return ans
