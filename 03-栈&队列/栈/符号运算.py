"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135005092

题目描述
给定一个表达式，求其分数计算结果。

表达式的限制如下：

所有的输入数字皆为正整数（包括0）
仅支持四则运算（+-*/）和括号
结果为整数或分数，分数必须化为最简格式（比如6，3/4，7/8，90/7）
除数可能为0，如果遇到这种情况，直接输出"ERROR"
输入和最终计算结果中的数字都不会超出整型范围
用例输入一定合法，不会出现括号匹配的情况

输入描述
字符串格式的表达式，仅支持+-*/，数字可能超过两位，可能带有空格，没有负数

长度小于200个字符

输出描述
表达式结果，以最简格式表达

如果结果为整数，那么直接输出整数
如果结果为负数，那么分子分母不可再约分，可以为假分数，不可表达为带分数
结果可能是负数，符号放在前面
用例1
输入
1 + 5 * 7 / 8
输出
43/8
用例2
输入
1 / (0 - 5)
输出
-1/5
说明
符号需要提到最前面

用例3
输入
1 * (3*4/(8-(7+0)))
输出
12
说明
注意括号可以多重嵌套


"""


# 获取输入
s = input()

# 数字栈
num_stack = []
# +-*/ 计算符号栈，还包括(
op_stack = []
# 符号优先级
op_priority = {'+': 1, '-': 1, '*': 2, '/': 2}


class FenShu:
    def __init__(self, fenzi, fenmu):
        self.fenzi = fenzi
        self.fenmu = fenmu

    def __repr__(self):
        return f'{self.fenzi}/{self.fenmu}'


def calc():
    # (3+4/5) 计算两个分数
    op = op_stack.pop()
    b = num_stack.pop()
    a = num_stack.pop()
    # 1/2 + 2/3
    if op == '+':
        fenmu = a.fenmu * b.fenmu
        fenzi = a.fenzi * b.fenmu + b.fenzi * a.fenmu
    elif op == '-':
        fenmu = a.fenmu * b.fenmu
        fenzi = a.fenzi * b.fenmu - b.fenzi * a.fenmu
    elif op == '*':
        fenmu = a.fenmu * b.fenmu
        fenzi = a.fenzi * b.fenzi
    elif op == '/':
        fenmu = a.fenmu * b.fenzi
        fenzi = a.fenzi * b.fenmu

    # 将计算得到的结果压栈
    num_stack.append(FenShu(fenzi, fenmu))


def calc_gys(a, b):
    # 计算2个数的最大公因数 12,15
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


def main():
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            # 多位数
            while i+1 < len(s) and s[i+1].isdigit():
                c += s[i+1]
                i += 1
            num_stack.append(FenShu(int(c), 1))
        elif c in '+-*/':
            # todo 判断符号优先级，
            # 如果符号栈顶的优先级更高，或者相同，则先弹出栈顶数字和符号进行计算
            # 反之先压栈
            while op_stack and op_stack[-1] != '(' and op_priority[op_stack[-1]] >= op_priority[c]:
                # (1 + 5 * 7 / 8)
                calc()
            op_stack.append(c)

        elif c == '(':
            op_stack.append(s[i])
        elif c == ')':
            # todo 反括号处理(3+4/2)
            while op_stack[-1] != '(':
                calc()
            op_stack.pop()

        i += 1

    # print(num_stack)
    # print(op_stack)

    # 没有括号
    # [1/1, 35/1, 8/1]
    # ['+', '/']
    while len(num_stack) > 1:
        calc()

    fenshu = num_stack[0]

    # 如果结果的分母为0（除数为0），则不合法
    if fenshu.fenmu == 0:
        return "ERROR"

    # 判断最后结果是正数还是负数
    sign = -1 if fenshu.fenzi * fenshu.fenmu < 0 else 1

    # 求分子、分母的最大公约数，并进行约份，求得最简格式的分子，分母
    fenshu.fenzi = abs(fenshu.fenzi)
    fenshu.fenmu = abs(fenshu.fenmu)
    gys = calc_gys(fenshu.fenzi, fenshu.fenmu)
    fenshu.fenzi //= gys
    fenshu.fenmu //= gys

    # 结果为整数或分数，分数必须化为最简格式（比如6，3/4，7/8，90/7）
    fenshu.fenzi *= sign
    if fenshu.fenmu == 1:
        return fenshu.fenzi
    else:
        return f'{fenshu.fenzi}/{fenshu.fenmu}'


print(main())
