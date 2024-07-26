"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135730137

OJ用例
题解 - 模拟数据序列化传输 - Hydro

题目描述
模拟一套简化的序列化传输方式，请实现下面的数据编码与解码过程

编码前数据格式为 [位置,类型,值]，多个数据的时候用逗号分隔，位置仅支持数字，不考虑重复等场景；类型仅支持：Integer / String / Compose（Compose的数据类型表示该存储的数据也需要编码）

编码后数据参考图示，数据区的格式是：位置#类型#长度#数据，类型存储需要编码，Integer->0；String->1；Compose->2，长度是指数据的字符长度；数据仅允许数字、大小写字母、空格。image

输入的编码字符长度不能超过1000，一个数据的格式错误，则解析剩下数据，其他错误输出ENCODE_ERROR。

输入的解码字符不能超过1000，数据区异常则跳过继续解析剩余数据区，其他异常输出DECODE_ERROR。

输入描述
输入有两行：
    第一行是命令，1表示编码，2表示解码
    第二行输入待编码、解码的字符
    数据最多嵌套10层，[1,Compose,[1,String,Second]] 为2层嵌套。

输出描述
    如果输入要求是编码，则输出编码结果；
    如果输入要求是解码，则输出解码结果；
    当异常时输出对应的错误字符。

用例1
输入
1
[1,String,I am Mary],[2,Integer,23],[3,Long,1000000],[4,Compose,[1,String,I am Kitty],[2,Integer,44]]
输出
1#1#9#I am Mary2#0#2#234#2#25#1#1#10#I am Kitty2#0#2#44
说明
由于Long型为不支持类型，所以数据[3,Long,1000000]自动被过滤掉

用例2
输入
2
1#1#9#I am Mary2#0#2#233#0#3#8794#2#25#1#1#10#I am Kitty2#0#2#44
输出
[1,String,I am Mary],[2,Integer,23],[3,Integer,879],[4,Compose,[1,String,I am Kitty],[2,Integer,44]]

用例3
输入
2
xxx
输出
DECODE_ERROR
说明
输入的待解码数据不满足格式要求

用例4
输入
1
[1,String,I am Mary],[2,Integer,23]],
输出
ENCODE_ERROR
说明
输入格式不满足输入格式要求
"""

import re

# 输入
# 1表示编码，2表示解码
# cmd = int(input())
# 待编码/解码的字符
# s = input()

# 测试数据
cmd = 1
# s = '[1,String,I am Mary],[2,Integer,23],[3,Long,1000000],[4,Compose,[1,String,I am Kitty],[2,Integer,44]]'
# s = '[1,String,I am Mary],[2,Integer,23]],'
s = '1#1#9#I am Mary2#0#2#233#0#3#8794#2#25#1#1#10#I am Kitty2#0#2#44'

# 输出：编码/解码结果
typ2nbr = {'Integer': '0', 'String': '1', 'Compose': '2'}
nbr2typ = {'0': 'Integer', '1': 'String', '2': 'Compose'}
# 编码前数据格式为 [位置,类型,值]
# 数据区的格式是：位置#类型#长度#数据，类型存储需要编码
# 1.位置仅支持数字，不考虑重复等场景
p_num = r'^\d+$'
# 2.类型仅支持：Integer / String / Compose
# 3.数据仅允许数字、大小写字母、空格
p_str = r'^[\dA-Za-z\s]+$'


def check_encode_str(s: str):
    '''校验要编码的字符串s有没有非数据格式错误'''
    # 输入的编码字符长度不能超过1000，一个数据的格式错误，则解析剩下数据，其他错误输出ENCODE_ERROR。
    # todo 字符串的replace方法不能使用正则匹配模式, 只能用re.sub方法
    # s2 = s.replace('[^[\]]', '')
    res = re.sub('[^[\]]', '', s)
    # print(res)

    # 利用stack校验是不是非格式错误
    stack = []
    for c in res:
        if c == '[':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()

    return True if not stack else False


def check_encode(pos, typ, val):
    '''校验要编码的字符串3个位置有没有数据格式错误'''
    if not re.match(p_num, pos):
        return False
    if typ not in typ2nbr:
        return False

    if typ == 'Integer':
        return re.match(p_num, val)
    elif typ == 'String':
        return re.match(p_str, val)

    return True


def encode(s: str):
    '''将s字符串按照规则编码'''
    s = s.replace('],[', '][')
    if not check_encode_str(s):
        return 'ENCODE_ERROR'

    # todo 正则表达式：匹配s中'[]'没有嵌套'[]'的数据
    p = r'\[([^\[\]]+)\]'
    # todo re.match是从s开头第一个字符开始查找p，re.search是从s所有位置查找p
    m = re.search(p, s)
    # print(m[0])
    while m:
        pos, typ, val = m.group(1).split(',')
        # print(pos, typ, val, sep=',')
        res = []  # res记录编码内容
        if check_encode(pos, typ, val):
            res.append(pos)
            res.append(typ2nbr[typ])
            res.append(str(len(val)))
            res.append(val)

        # todo 将s中匹配到的字符串，替换为编码内容res
        s = s.replace(m[0], '#'.join(res))
        # print(s)
        # 继续查找下一个[]
        m = re.search(p, s)
        # print(m)
    return s

# print(encode(s))


def check_decode(pos, typ, sz, val):
    '''校验要解码的s有没有数据格式错误'''
    if not re.match(p_num, pos):
        return False
    if typ not in nbr2typ:
        return False

    if typ == '0':
        return re.match(p_num, val)
    elif typ == '1':
        return re.match(p_str, val)

    return True


def decode(s):
    '''解码s:
    1、各数据区之间没有分隔符，即无法直接分离出各个数据区
    2、Compose类型数据区的"数据"部分也是一个或多个数据区组合
    '''
    dq = s.split('#')
    # print(dq)

    ans = []  # res代表解码之后的结果列表
    while dq:
        print(f'dq={dq}')
        # 前3个分别代表pos, typ, sz
        pos = dq.pop(0)
        typ = dq.pop(0)
        sz = int(dq.pop(0))

        # 第4个需要判断数据类型是不是Compose
        # 并且val要截取正确的长度
        remain = '#'.join(dq)
        val = remain[:sz]
        dq.clear()
        if sz < len(remain):
            remain = remain[sz:]
            dq = remain.split('#')

        if typ == '2':
            val = decode(val)

        if check_decode(pos, typ, sz, val):
            ans.append(f'[{pos},{nbr2typ[typ]},{val}]')

        print(f' ans={ans}')

    return ','.join(ans)


# print(decode(s))
def main():
    if cmd == 1:
        return encode(s)
    else:
        try:
            res = decode(s)
            return res
        except:
            return 'DECODE_ERROR'


print(main())
