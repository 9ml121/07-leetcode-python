"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

补充：
输入：
s = "([)]"
输出：
false

提示：
1 <= s.length <= 10^4
s 仅由括号 '()[]{}' 组成
"""

# todo 简单的栈应用问题

# 方法1：栈
class Solution:
    def isValid(self, s: str) -> bool:
        # 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效
        
        # todo 栈用来保存左括号
        st = []
        mp = {
            ')': '(', 
            '}': '{', 
            ']': '['
            }
        
        for c in s:
            if c in mp:
                # 右括号：判断st栈顶元素是不是对应左括号
                if not st or st[-1] != mp[c]:
                    return False
                else:
                    st.pop()
            else:
                # 左括号
                st.append(c)

        # 最后判断有没有多余左括号
        return not st

# 方法2:正则匹配
class Solution:
    def isValid(self, s: str) -> bool:
        # 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效
        # 不断通过消除 '[]' ， '()', '{}' ，最后判断剩下的是否是空串即可，就像开心消消乐一样。
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return not s

