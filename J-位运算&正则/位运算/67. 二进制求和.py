"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。


示例 1：
输入:a = "11", b = "1"
输出："100"

示例 2：
输入：a = "1010", b = "1011"
输出："10101"


提示：

1 <= a.length, b.length <= 104
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
"""


# 方法1：二进制转整数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# 方法2：模拟加法
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        n = max(len(a), len(b))
        carry = 0
        for i in range(n):
            carry += (int(a[len(a) - i - 1]) if i < len(a) else 0)
            carry += (int(b[len(b) - i - 1]) if i < len(b) else 0)
            ans.append(carry % 2)
            carry //= 2

        if carry > 0:
            ans.append(carry)

        return ''.join(map(str, ans[::-1]))
