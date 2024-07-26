"""
给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。
你可以 按任意顺序 返回答案。
生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 10^4 。

示例 1：
输入：expression = "2-1-1"
输出：[0,2]
解释：
((2-1)-1) = 0
(2-(1-1)) = 2

示例 2：
输入：expression = "2*3-4*5"
输出：[-34,-14,-10,-10,10]
解释：
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


提示：
1 <= expression.n <= 20
expression 由数字和算符 '+'、'-' 和 '*' 组成。
输入表达式中的所有整数值在范围 [0, 99]
"""

from typing import List

# 按不同优先级组合数字和运算符
# 备忘录
memo = {}


def diffWaysToCompute(s: str) -> List[int]:
    # 避免重复计算
    if s in memo:
        return memo[s]

    # basecase:如果只剩下数字，返回单个数值的列表
    if s.isdigit():
        return [int(s)]

    res = []
    # 迭代字符串，以符号分治
    for i in range(len(s)):
        if s[i] in "+-*":
            # 递归字符串前半部分和后半部分
            left = diffWaysToCompute(s[:i])
            right = diffWaysToCompute(s[i + 1:])
            # 组合两个结果的值
            for j in left:
                for k in right:
                    if s[i] == "+":
                        res.append(j + k)
                    elif s[i] == "-":
                        res.append(j - k)
                    elif s[i] == "*":
                        res.append(j * k)
    # 将结果添加进备忘录
    memo[input] = res
    return res


if __name__ == '__main__':
    s = "2*3-4*5"
    print(diffWaysToCompute(s))
