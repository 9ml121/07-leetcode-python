"""
输入描述：
输入一行字符串，可以有空格

输出描述：
输出参数个数，分解后的参数，每个参数都独占一行

解析规则：

1.参数分隔符为空格
2.对于用""包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy /s "C:\\program files" "d:\"时，参数仍然是4个，
 第3个参数应该是字符串C:\\program files，而不是C:\\program，注意输出参数时，需要将""去掉，引号不存在嵌套情况。
3.参数不定长

4.输入由用例保证，不会出现不符合要求的输入
数据范围：字符串长度：1≤s≤1000
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
"""

# s = input()
s = '''xcopy /s "C:\\program files" "d:\"'''
# s = 'xcopy /s c:\\ d:\\e'

# tmp存储临时要解析的字符
tmp = ''
# res存储解析出来的参数
res = []
# 表示参数是否为引号内的标识
flag = False
flags = []
for v in s:
    if v != '"':
        tmp += v
    else:
        flags.append(flag)
        res.append(tmp)
        tmp = ''
        flag = not flag

flags.append(flag)
res.append(tmp)

# 进一步解析res，结果放进res2
res2 = []
for i in range(len(res)):
    if flags[i]:
        res2.append(res[i])
    else:
        res2.extend(res[i].split())

print(len(res2))
for i in res2:
    print(i)
