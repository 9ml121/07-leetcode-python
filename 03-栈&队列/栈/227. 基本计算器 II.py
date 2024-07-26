"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5


提示：
1 <= s.length <= 3 * 10^5
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
题目数据保证答案是一个 32-bit 整数
"""


class Solution:
    def calculate(self, s: str) -> int:
        num = 0  # 当前数字
        stack = []  # 存放数字的栈
        op = "+"  # 当前符号，初始化为 '+'

        for i, c in enumerate(s):
            # todo 字符串转整数
            if c.isdigit():
                num = num * 10 + int(c)

            # todo 处理乘除加减
            # 如果当前字符不是数字或者是字符串 s 的最后一个字符，则将当前数字 num 做对应运算并入栈
            # 自动忽略空格符
            if c in ('+', '-', '*', '/') or i == len(s) - 1:
                # 根据之前的符号来进行数字的运算
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif op == '/':
                    pre = stack.pop()
                    # stack.append(pre // num)  # 注意这个写法是错的，因为-3//2 = -2
                    stack.append(int(pre / num))

                # 更新符号为当前符号，数字清零
                op = c
                num = 0

        # print(stack)
        return sum(stack)


if __name__ == '__main__':
    s = " 3+5 / 2 "
    print(Solution().calculate(s))
