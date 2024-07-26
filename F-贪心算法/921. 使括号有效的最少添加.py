"""
只有满足下面几点之一，括号字符串才是有效的：
1.它是一个空字符串，
2.或者它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，
3.或者它可以被写作 (A)，其中 A 是有效字符串。

给定一个括号字符串 s ，在每一次操作中，你都可以在字符串的任何位置插入一个括号

例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
返回 为使结果字符串 s 有效而必须添加的最少括号数。

示例 1：
输入：s = "())"
输出：1

示例 2：
输入：s = "((("
输出：3


提示：
1 <= s.length <= 1000
s 只包含 '(' 和 ')' 字符。
"""

# 方法 1：贪心算法
"""
思路分析：
括号匹配的问题，其实我们并不陌生，「力扣」第 20 题、第 22 题都是类似的问题。我们在草稿纸上写下一个括号匹配的过程，可以发现：
1. 从左向右遍历的过程中，左括号出现是不受限制的；
2. 右括号出现的时候，一定在之前已经出现了数量 严格大于（等于是不可以的） 右括号数量的左括号；
3. 匹配的括号，最后一个字符一定是右括号。

「贪心算法」的直觉：
情况 1：左括号出现的时候，记录在当前位置的右边可能需要增加的右括号的数量 rightCount；
情况 2：右括号出现的时候，每一个右括号需要和之前已经出现的左括号配对：
    - 需要抵销「情况 1」中记录的右括号的数量；
    - 如果「情况 1」中记录的右括号的数量不够，就需要记录在当前位置的左边可能需要增加的右括号的数量 leftCount。
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        leftCount = 0  # 需要另外添加的左括号数量
        rightCount = 0  # 需要另外添加的右括号数量
        for c in s:
            if c == '(':
                rightCount += 1
            else:
                if rightCount == 0:
                    leftCount += 1
                else:
                    rightCount -= 1
        return leftCount + rightCount


# 写法 2
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        leftCount = 0
        res = 0
        for c in s:
            if c == '(':
                leftCount += 1
            else:
                if leftCount == 0:
                    res += 1
                else:
                    leftCount -= 1
        res += leftCount
        return res
