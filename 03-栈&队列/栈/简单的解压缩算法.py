"""
题目描述
现需要实现一种算法，能将一组压缩字符串还原成原始字符串，还原规则如下：

1、字符后面加数字N，表示重复字符N次。例如：压缩内容为A3，表示原始字符串为AAA。
2、花括号中的字符串加数字N，表示花括号中的字符重复N次。例如压缩内容为{AB}3，表示原始字符串为ABABAB。
3、字符加N和花括号后面加N，支持任意的嵌套，包括互相嵌套，例如：压缩内容可以{A3B1{C}3}3

输入描述
输入一行压缩后的字符串

输出描述
输出压缩前的字符串

备注
输入保证，数字不会为0，花括号中的内容不会为空，保证输入的都是合法有效的压缩字符串
输入输出字符串区分大小写
输入的字符串长度范围为[1, 10000]
输出的字符串长度范围为[1, 100000]
数字N范围为[1, 10000]

用例
输入	{A3B1{C}3}3
输出	AAABCCCAAABCCCAAABCCC
说明	{A3B1{C}3}3代表A字符重复3次，B字符重复1次，花括号中的C字符重复3次，最外层花括号中的AAABCCC重复3次。
"""

# todo 04-栈&队列\栈\394. 字符串解码.py 
'''
题目解析
本题似曾相识，和下面两个题目很像
    04-栈&队列\栈\一种字符串压缩表示的解压.py
    04-栈&队列\栈\报文解压缩.py
做完本题后，可以尝试再做做上面这两个真题。

本题可以使用栈结构来解题。
注意：有可能重复2位数以上
'''

# 测试数据
s1 = '{A2{BC}2}2'
s2 = '{ab}2'
s3 = '{a10}3b2'
s4 = 'a2{b}2'
s = 'A10B1{DC}3'

# 输入：压缩后的字符串
# s = input()

# 输出：压缩前的字符串
s += ' '    # 方便遍历条件判断
stack = []  # 保存所有已遍历字符
idxs = []   # 保存已遍历字符'{'在 stack的索引下标
repeat = 0  # 记录重复次数
for c in s:
    # 1. 处理重复次数
    if c.isdigit():
        repeat = repeat * 10 + int(c)
        continue

    if repeat > 0:
        top_c = stack.pop()
        if top_c != '}':
            # 处理 A10 这样的内容
            stack.append(top_c * repeat)
        else:
            # 处理'{}'里面内容
            start = idxs.pop()  # 左括号在 stack中的索引下标
            s = ''.join(stack[start+1:])
            stack = stack[:start] # stack需要切掉{}里的内容
            stack.append(s * repeat) # stack加上解码之后的内容
        repeat = 0

    if c == '{':
        idxs.append(len(stack))

    stack.append(c)

# print(stack)
ans = ''.join(stack).strip()
print(ans)
