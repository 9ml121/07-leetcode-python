"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

提示：

m == s.n
n == t.n
1 <= m, n <= 105
s 和 t 由英文字母组成

进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
"""
import collections
from math import inf

# todo 不固定长度滑窗 + 计数器


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。"""
        # 记录t中每个字符的出现次数
        need = collections.Counter(t)
        # 记录t中不同字符的总数
        need_cnt = len(need)

        # 要求的最小覆盖子串为 s[start..start+min_len)
        start = 0  # 最小覆盖子串的起始位置 start
        min_len = inf  # 最小覆盖子串长度 min_len，初始值为一个不可能达到的值

        # todo 循环不变量：[l..r]窗口里的元素是涵盖 t 所有字符的子串
        l = 0
        for r, c in enumerate(s):
            # 入
            if c in need:
                need[c] -= 1
                # 如果该字符的出现次数减为0，说明已经找到了一个需要的字符，更新needCnt
                if need[c] == 0:
                    need_cnt -= 1

            # 出
            while need_cnt == 0:
                # 更新ans: 最小子串长度和起始位置
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                # 如果左指针的字符在t中出现过，更新need中对应字符的出现次数
                remove = s[l]
                if remove in need:
                    need[remove] += 1
                    # 如果该字符的出现次数增加为1，说明需要的字符不再全部被包含在子串中，更新needCnt
                    if need[remove] > 0:
                        need_cnt += 1
                # 移动左指针
                l += 1

        # 如果结果变量始终未被更新，说明不存在满足条件的子串
        return s[start:start + min_len] if min_len != inf else ""


if __name__ == '__main__':
    cls = Solution()
    s = "DAOBECODEBANC"
    t = "ABC"
    print(cls.minWindow(s, t))
