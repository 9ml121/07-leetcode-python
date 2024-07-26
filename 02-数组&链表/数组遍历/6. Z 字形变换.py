"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"
 

提示：
1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
"""

# todo 巧设flag
"""
设 numRows 行字符串分别为 s1, s2.., sn
​则容易发现：按顺序遍历字符串 s 时，每个字符 c 在 N 字形中对应的 行索引 先从 s1 增大至 sn，再从 sn 减小至 s1  …… 如此反复。

因此解决方案为：模拟这个行索引的变化，在遍历 s 中把每个字符填到正确的行 ans[i] 。
"""


# 写法1:最简洁   
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
        ans = [''] * numRows

        i = 0       # i指向ans数组下一个需要写入字符的索引位置
        flag = -1   # flag是一个只为-1和1的整数，用来切换遍历方向（从上往下 <-> 从左到右）
        for c in s:
            ans[i] += c

            if i == 0 or i == numRows-1:
                flag = -flag

            i += flag

        return ''.join(ans)

# 写法2：
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
        ans = [''] * numRows

        i = 0    # i指向ans数组下一个需要写入字符的索引位置
        flag = 0  # flag是一个布尔整数，用来切换遍历方向（从上往下 <-> 从左到右）
        for c in s:
            ans[i] += c

            if i == numRows-1:
                flag = 1
            if i == 0:
                flag = 0

            if not flag:
                i += 1
            else:
                i -= 1

        return ''.join(ans)
