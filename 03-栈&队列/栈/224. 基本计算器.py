"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23


提示：
1 <= s.length <= 3 * 10^5
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
'+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
'-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
输入中不存在两个连续的操作符
每个数字和运行的计算将适合于一个有符号的 32位 整数
"""


# 参考：https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-shi--24fe4/
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        num = 0
        for c in s:
            if c == " ":
                continue

            # todo 1.字符串转整数
            elif c.isdigit():
                num = num * 10 + int(c)

            # todo 2.处理加减法
            elif c == '+' or c == "-":
                res += sign * num
                num = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1

            # todo 3.处理括号
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            # 每个")"都对应一个前面的"("
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        return res + sign * num


if __name__ == '__main__':
    # s = "1-(     -2)"
    # s = "1 + 1"
    # s = " 2-1 + 2 "
    s = "(1+(4+5+2)-3)+(6+8)"  # 23
    print(Solution().calculate(s))
