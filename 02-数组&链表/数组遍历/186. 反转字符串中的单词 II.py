"""
给你一个字符数组 s ，反转其中 单词 的顺序。

单词 的定义为：单词是一个由非空格字符组成的序列。s 中的单词将会由单个空格分隔。

必须设计并实现 原地 解法来解决此问题，即不分配额外的空间。



示例 1：

输入：s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出：["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
示例 2：

输入：s = ["a"]
输出：["a"]


提示：

1 <= s.length <= 105
s[i] 可以是一个英文字母（大写或小写）、数字、或是空格 ' ' 。
s 中至少存在一个单词
s 不含前导或尾随空格
题目数据保证：s 中的每个单词都由单个空格分隔
"""
from typing import List

# todo 两次反转法
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # 自己实现arr.reverse()函数
        def reverse_s(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        n = len(s)
        # 1.先整体反转一次s
        reverse_s(0, n-1)

        # 2.再反转s中每个单词：以空格为分界点
        i = 0
        for j in range(n):
            if s[j] == ' ':
                reverse_s(i, j-1)
                i = j + 1

        # 反转最后一个单词
        reverse_s(i, n-1)
