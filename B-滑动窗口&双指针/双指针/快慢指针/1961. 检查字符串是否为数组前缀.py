"""
给你一个字符串 s 和一个字符串数组 words ，请你判断 s 是否为 words 的 前缀字符串 。

字符串 s 要成为 words 的 前缀字符串 ，需要满足：s 可以由 words 中的前 k（k 为 正数 ）个字符串按顺序相连得到，且 k 不超过 words.length 。

如果 s 是 words 的 前缀字符串 ，返回 true ；否则，返回 false 。

 

示例 1：
输入：s = "iloveleetcode", words = ["i","love","leetcode","apples"]
输出：true
解释：
s 可以由 "i"、"love" 和 "leetcode" 相连得到。

示例 2：
输入：s = "iloveleetcode", words = ["apples","i","love","leetcode"]
输出：false
解释：
数组的前缀相连无法得到 s 。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] 和 s 仅由小写英文字母组成
"""


from typing import List
# todo 方法2：简单的快慢双指针(推荐)


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # 判断 s 是否可以由 words 中的前 k（k 为 正数 ）个字符串按顺序相连得到
        # si指向s下一个需要匹配的字符
        si = 0

        # 遍历words列表每个单词的每个字符c:
        for w in words:
            for c in w:
                # 如果c和s[si]相同，si右移，否则不满足前缀条件，直接返回False
                if si >= len(s) or s[si] != c:
                    return False
                si += 1

            # 如果si==len(s),证明s中的所有字符都在words前缀中，直接返回True
            if si == len(s):
                return True

        # 遍历完成 words 时 s 仍未遍历完成
        return False



# 方法1：字符串函数
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # 判断 s 是否可以由 words 中的前 k（k 为 正数 ）个字符串按顺序相连得到
        res = ''
        for w in words:
            res += w
            if res == s:
                return True
            
            if not s.startswith(res):
                return False

        return False

