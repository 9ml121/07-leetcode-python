"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：

输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：

输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
 

提示：

1 <= s.length, t.length <= 200
s 和 t 只含有小写字母以及字符 '#'
 

进阶：

你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""
# todo 方法1：栈（空间复杂度O(m+n),最好理解）


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 比较含退格的字符串是否相等
        def convert(s: str) -> str:
            st = []
            for c in s:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)

            return ''.join(st)

        s = convert(s)
        t = convert(t)

        return s == t


# todo 方法2：同向双指针（最优解！）
# 类似：B-滑动窗口&双指针\双指针\快慢指针\925. 长按键入.py

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 比较含退格的字符串是否相等
        i = len(s) - 1
        j = len(t) - 1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                # todo 注意这里的循环逻辑："ab##","c#d#"; "bxj##tw","bxo#j##tw"
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i < 0 and j >= 0) or (i >= 0 and j < 0):
                return False

            i -= 1
            j -= 1

        return True
            
        

