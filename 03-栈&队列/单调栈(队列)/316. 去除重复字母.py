"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"


提示：

1 <= s.n <= 104
s 由小写英文字母组成
"""
import collections

'''
题目的要求总结出来有三点：
要求一、要去重。
要求二、去重字符串中的字符顺序不能打乱 s 中字符出现的相对顺序。
要求三、在所有符合上一条要求的去重字符串中，字典序最小的作为最终结果

要求一、通过 last_idxs字典或者一个26位数组记录每个字符在s中最后出现的位置
要求二、我们顺序遍历字符串 s，通过「栈」这种顺序结构的 push/pop 操作记录结果字符串，保证了字符出现的顺序和 s 中出现的顺序一致。
    这里也可以想到为什么要用「栈」这种数据结构，因为先进后出的结构允许我们立即操作刚插入的字符，如果用「队列」的话肯定是做不到的。
要求三、我们用类似单调栈的思路，配合计数器 count 不断 pop 掉不符合最小字典序的字符，保证了最终得到的结果字典序最小。
'''


# todo 使用单调栈来维护去除「关键字符」后得到的字符串并记录字符出现的顺序
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
