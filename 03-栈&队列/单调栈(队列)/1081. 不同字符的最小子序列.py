"""
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同



示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"


提示：

1 <= s.length <= 1000
s 由小写英文字母组成
"""


# 参考：04-栈 & 队列\单调栈(队列)\316. 去除重复字母.py 一样的题
import collections

# 写法1：单调栈 + 字典
class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        """去除字符串中重复的字母,  返回结果的字典序最小
        （要求不能打乱其他字符的相对位置）。
        """
        # last_idxs保存每个字符最后一次出现的索引，可以用字典或者26位数组表示
        last_idxs = {}
        for i, c in enumerate(s):
            last_idxs[c] = i

        # st保留s中不重复的字符，能够保证字符添加有序，且是字典最小序排列
        st = []
        # 再遍历一次s,去除重复字符。并保证字典序最小
        for i, c in enumerate(s):
            if c in st:
                # 栈中元素不重复
                continue

            # todo 弹出栈顶元素条件:
            # ① 栈非空，
            # ② 当前元素字典序 < 栈顶元素，
            # ③ 栈顶元素在以后还会出现，
            while st and c < st[-1] and i < last_idxs[st[-1]]:
                st.pop()

            st.append(c)
        return ''.join(st)


# 写法2: 单调栈 + 计数器
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """去除字符串中重复的字母,  返回结果的字典序最小
        （要求不能打乱其他字符的相对位置）。
        """
        # st保留s中不重复的字符，能够保证字符添加有序，且是字典最小序排列
        st = []
        # 使用计数器统计s中可以使用的单词个数
        char_cnt = collections.Counter(s)

        for c in s:
            if c in st:
                # 栈中元素不重复
                char_cnt[c] -= 1
                continue

            while st and c < st[-1] and char_cnt[st[-1]] > 0:
                # 栈顶元素比当前元素大，且在后面还会出现
                st.pop()

            st.append(c)
            char_cnt[c] -= 1
        return ''.join(st)


if __name__ == '__main__':
    # s = 'bcabc'  # anc
    s = "cdadabcc"  # "adbc"
    print(Solution().removeDuplicateLetters(s))
