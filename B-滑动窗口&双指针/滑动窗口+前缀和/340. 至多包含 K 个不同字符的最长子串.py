"""
给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。



示例 1：

输入：s = "eceba", k = 2
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。
示例 2：

输入：s = "aa", k = 1
输出：2
解释：满足题目要求的子串是 "aa" ，长度为 2 。


提示：

1 <= s.length <= 5 * 104
0 <= k <= 50
"""
import collections
# todo 不定长滑窗 + 计数器

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # 找出 s至多 包含 k 个 不同 字符的最长子串长度
        ans = 0
        win_dict = collections.Counter()
        dict_len = 0
        
        l = 0
        for r, c in enumerate(s):
            # 入
            if win_dict[c] == 0:
                dict_len += 1
            win_dict[c] += 1
            
            # 出
            while dict_len > k:
                win_dict[s[l]] -= 1
                if win_dict[s[l]] == 0:
                    dict_len -= 1
                l += 1

            # 更新ans
            ans = max(ans, r - l + 1)

        return ans
