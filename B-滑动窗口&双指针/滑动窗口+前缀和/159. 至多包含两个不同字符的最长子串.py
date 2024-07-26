"""
给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长子串，并返回该子串的长度。
 

示例 1：
输入：s = "eceba"
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。
示例 2：

输入：s = "ccaabbb"
输出：5
解释：满足题目要求的子串是 "aabbb" ，长度为 5 。
 

提示：

1 <= s.length <= 105
s 由英文字母组成
"""


import collections

# todo 不定长滑窗 + 计数器
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 返回滑窗内至多包含2个​不同字符的最长子串,
        ans = 0
        # win_cnts维护滑窗内元素：个数, dict_len维护窗口元素集合个数
        win_dict = collections.Counter()
        dict_len = 0
        
        l = 0
        for r, c in enumerate(s):
            # 入
            if win_dict[c] == 0:
                dict_len += 1
            win_dict[c] += 1
            
            # 出
            while dict_len > 2:
                win_dict[s[l]] -= 1
                if win_dict[s[l]] == 0:
                    dict_len -= 1
                l += 1

            # 更新ans
            ans = max(ans, r - l + 1)

        return ans
