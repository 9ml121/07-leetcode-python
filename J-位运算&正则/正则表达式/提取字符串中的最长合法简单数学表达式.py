"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134454049

OJ用例
https://hydro.ac/d/HWOD2023/p/OD340/solution

题目描述
提取字符串中的最长合法简单数学表达式，字符串长度最长的，并计算表达式的值。如果没有，则返回 0 。

简单数学表达式只能包含以下内容：

0-9数字，符号+-*
说明：

所有数字，计算结果都不超过long
如果有多个长度一样的，请返回第一个表达式的结果
数学表达式，必须是最长的，合法的
操作符不能连续出现，如 +--+1 是不合法的
输入描述
字符串

输出描述
表达式值

用例1
输入
1-2abcd
输出
-1
说明
最长合法简单数学表达式是"1-2"，结果是-1
"""

import re
'''
题意有点模糊，按照测试用例推断：
操作符不能连续出现，代表只包含两个操作数的运算表达式，比如：
a + b
a - b
a * b

特殊测试用例：
1+2++3+4+5 ==》 +3+4
1+2*31+41+51+abc++1234567890++  ==》+41+51
a1+21abc-3+40 ==》 -3+40
'''

# 获取输入
# s = input()
# s = '1+2+a+2c*15+7*500'
# s = '1+2++3+4+5'

# 方法1: 正则 + 栈


def main1(s):
    n = len(s)
    nums = []
    maxLen = 0  # 有效表达式的最大长度
    ans = ''
    r = 0
    while r < n:
        if s[r].isdigit():  # 500
            num = s[r]
            while r+1 < n and s[r+1].isdigit():
                r += 1
                num += s[r]

            # if len(nums) >= 2 and nums[-1] in '+-*' and nums[-2].isdigit(): # '-1' 不算digit
            # '-1' 不算digit
            if len(nums) >= 2 and nums[-1] in '+-*' and re.match(r'^[+-]?\d+$', nums[-2]):
                # 找到1个有效表达式， 计算长度
                sz = len(nums[-2]) + len(num)
                if sz > maxLen:
                    maxLen = sz
                    ans = nums[-2] + nums[-1] + num
                    # print(ans)

            # 拼接正负号
            if len(nums) > 0 and nums[-1] in '+-':
                nums[-1] = nums[-1] + num
            else:
                nums.append(num)

        elif s[r] in '+-*':
            nums.append(s[r])
        else:
            nums.clear()

        r += 1

    # print(eval(ans)) if ans else print(0)


# 方法2: 正则 + 双指针
def main2():
    # 下面正则可得90%+通过率
    # reg = re.compile(r"^(-?\d+)([+*-])(\d+)$")

    # 下面正则应该可得100%通过率，如果不行再用前面正则
    reg = re.compile(r"^([+-]?\d+)([+*-])(\d+)$")

    maxExpLen = 0
    ans = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            subStr = s[i:j + 1]

            if reg.match(subStr) and len(subStr) > maxExpLen:
                maxExpLen = len(subStr)

                match = reg.search(subStr)

                op_num1 = int(match.group(1))
                op = match.group(2)
                op_num2 = int(match.group(3))

                if op == "*":
                    ans = op_num1 * op_num2
                elif op == "+":
                    ans = op_num1 + op_num2
                elif op == "-":
                    ans = op_num1 - op_num2

    return ans

# 算法调用
# print(main2())


# todo 正则测试  注意()表示捕获组，(?:)表示非捕获组， 捕获组和非捕获组的区别在于，是否需要捕获（）里的内容
s = '+1+2+a+2c*15+7*500'

lst1 = re.compile(r'[+-]?\d+[+*-]\d+')
# print(lst1)  # ['1+2', '15+7']

# 下面正则无法匹配这样的数字串：+1+2
lst2 = re.compile(r"((?:\d+[+*-])*\d+)").findall(s)
print(lst2)  # ['1+2', '2', '15+7*500']

# 下面正则可以匹配到这样的数字串：+1+2
lst3 = re.compile(r"([+-]?(?:\d+[+*-])*\d+)").findall(s)
print(lst3)  # ['+1+2', '+2', '15+7*500']

s = '+7*500'
lst4 = re.compile(r"^([+-]?\d+)([+*-])(\d+)$").findall(s)
# print(lst4)  # [('+7', '*', '500')]
