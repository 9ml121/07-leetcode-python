"""
给定两个字符串 s 和 t ，如果它们的编辑距离为 1 ，则返回 true ，否则返回 false 。

字符串 s 和字符串 t 之间满足编辑距离等于 1 有三种可能的情形：

往 s 中插入 恰好一个 字符得到 t
从 s 中删除 恰好一个 字符得到 t
在 s 中用 一个不同的字符 替换 恰好一个 字符得到 t


示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
示例 2:

输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。


提示:

0 <= s.length, t.length <= 104
s 和 t 由小写字母，大写字母和数字组成
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns > nt:  # 保证s长度不超过t
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:  # t比s长度大于1，返回False
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return ns + 1 == nt  # 排除s==t


