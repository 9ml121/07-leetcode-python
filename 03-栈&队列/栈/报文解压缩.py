"""
题目描述
为了提升数据传输的效率，会对传输的报文进行压缩处理。
输入一个压缩后的报文，请返回它解压后的原始报文。
压缩规则：n[str]，表示方括号内部的 str 正好重复 n 次。
注意 n 为正整数（0 < n <= 100），str只包含小写英文字母，不考虑异常情况。

输入描述
输入压缩后的报文：

1）不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的；
2）原始报文不包含数字，所有的数字只表示重复的次数 n ，例如不会出现像 5b 或 3[8] 的输入；

输出描述
解压后的原始报文

注：原始报文长度不会超过1000，不考虑异常的情况

用例
输入	3[k]2[mn]
输出	kkkmnmn
说明	k 重复3次，mn 重复2次，最终得到 kkkmnmn

输入	3[m2[c]]
输出	mccmccmcc
说明	m2[c] 解压缩后为 mcc，重复三次为 mccmccmcc
"""

# todo 类似04-栈&队列\栈\简单的解压缩算法.py

# 测试数据
# s = '2[bm12[c]]'
s = '10[ck]2[mn]'
# s = '3[k]2[mn]'
# s = '3[m2[c]]'

# 输出：解压后的报文
stack = []  # 记录已遍历的所有字符
idxs = []  # 记录左括号在stack中的位置
repeat = 0  # 记录重复子串的重复次数
for c in s:
    if c.isdigit():
        repeat = repeat * 10 + int(c)
        continue
    
    # 1.stack保存重复次数
    if repeat > 0:
        stack.append(repeat)
        repeat = 0

    # 2.stack保存‘[’和字母
    if c == '[' or c.isalpha():
        # 记录’['在stack位置
        if c == '[':
            idxs.append(len(stack))
        stack.append(c)
    else:
        # 3. c == ']': 解码重复字符
        start = idxs.pop()  # 左括号在stack的下标
        sub = ''.join(stack[start+1:])  # 括号内的字符串
        stack = stack[:start]  # stack需要先移除括号内容
        # '['的前面必然是重复次数
        num = stack.pop()
        stack.append(sub * num)


print(''.join(stack))
