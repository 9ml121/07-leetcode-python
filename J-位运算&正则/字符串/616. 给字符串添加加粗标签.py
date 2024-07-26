"""
给定字符串 s 和字符串数组 words。

对于 s 内部的子字符串，若其存在于 words 数组中， 则通过添加闭合的粗体标签 <b> 和 </b> 进行加粗标记。

如果两个这样的子字符串重叠，你应该仅使用一对闭合的粗体标签将它们包围起来。
如果被粗体标签包围的两个子字符串是连续的，你应该将它们合并。
返回添加加粗标签后的字符串 s 。



示例 1：

输入： s = "abcxyz123", words = ["abc","123"]
输出："<b>abc</b>xyz<b>123</b>"
解释：两个单词字符串是 s 的子字符串，如下所示: "abcxyz123"。
我们在每个子字符串之前添加<b>，在每个子字符串之后添加</b>。
示例 2：

输入：s = "aaabbcc", words = ["aaa","aab","bc"]
输出："<b>aaabbc</b>c"
解释：
"aa"作为子字符串出现了两次: "aaabbb" 和 "aaabbb"。
"b"作为子字符串出现了三次: "aaabbb"、"aaabbb" 和 "aaabbb"。
我们在每个子字符串之前添加<b>，在每个子字符串之后添加</b>: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>"。
由于前两个<b>重叠，把它们合并得到: "<b>aaa</b><b>b</b><b>b</b><b>b</b>"。
由于现在这四个<b>是连续的，把它们合并得到: "<b>aaabbb</b>"。


提示：

1 <= s.length <= 1000
0 <= words.length <= 100
1 <= words[i].length <= 1000
s 和 words[i] 由英文字母和数字组成
words 中的所有值 互不相同

注：此题与「758 - 字符串中的加粗单词」相同 - https://leetcode-cn.com/problems/bold-words-in-string
"""
from typing import List

"""
解题思路：
我们可以使用一个布尔数组 bold 来标记字符串 s 中每个字符是否需要加粗。
遍历字符串 s，对于每一个字符串 dict 中出现的单词，我们在 bold 数组中将对应区间内的字符标记为 True。

接下来，我们根据 bold 数组生成最终的加粗字符串。
遍历 s，当遇到一个需要加粗的起点时，在结果字符串中添加 <b> 标签。
当遇到一个需要加粗的终点时，在结果字符串中添加 </b> 标签。
"""


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        isBold = [False] * n

        for word in words:
            start = -1
            while True:
                start = s.find(word, start + 1)  # 关键步骤
                if start == -1:
                    break
                for i in range(start, start + len(word)):
                    isBold[i] = True

        # print(isBold)
        res = ''
        i = 0
        while i < n:
            if isBold[i]:
                res += '<b>'
                while i < n and isBold[i]:
                    res += s[i]
                    i += 1
                res += '</b>'
            else:
                res += s[i]
                i += 1
        return res
