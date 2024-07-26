"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
 

提示：

1 <= name.length, typed.length <= 1000
name 和 typed 的字符都是小写字母
"""
# todo 同向双指针
# 类似：B-滑动窗口&双指针\双指针\快慢指针\844. 比较含退格的字符串.py

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # 判断name和typed是否一样（typed可能重复输入一个字符）
        n = len(name)
        m = len(typed)
        i = 0  # 指向name
        j = 0  # 指向types

        while i < n or j < m:
            if i < n and j < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and j < m and typed[j] == typed[j-1]:
                # typed重复输入
                j += 1
            else:
                return False

        return True
